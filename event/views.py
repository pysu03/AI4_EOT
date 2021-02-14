from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.views import generic

from .forms import EventForm
from .models import Event
from .utils import Calendar
from core.utils import get_date, prev_month, next_month


@login_required(login_url='signin')
def create_event(request):
    form = EventForm(request.POST or None)
    if request.POST and form.is_valid():
        title = form.cleaned_data['title']
        description = form.cleaned_data['description']
        time = form.cleaned_data['time']
        address = form.cleaned_data['address']
        completed = form.cleaned_data['completed']

        Event.objects.get_or_create(
            user=request.user,
            title=title,
            description=description,
            time=time,
            address=address,
            completed=completed,
        )
        return redirect('/')
    return render(request, 'event/event.html', {'form': form})

class EventEdit(generic.UpdateView):
    model = Event
    fields = ['title', 'description', 'time', 'address']
    template_name = 'event/event.html'

@login_required(login_url='signin')
def event_details(request, event_id):
    event = Event.objects.get(id=event_id)
    context = {
        'event': event
    }
    return render(request, 'event/event_details.html', context)


def saveNback(request):
    id = request.POST['id']
    saveCB = request.POST['saveCB']
    event = Event.objects.get(id=id)
    event.completed = saveCB
    event.save()
    return redirect('/')