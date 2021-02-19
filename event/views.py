from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.views import generic

from .forms import EventForm
from .models import Event
from .utils import Calendar
from core.utils import get_date, prev_month, next_month

def event(request):
    user = request.user.id
    context = {}
    d = get_date(request.GET.get('month', None))
    cal = Calendar(d.year, d.month)
    cal.setfirstweekday(6)
    html_cal = cal.formatmonth(user, withyear=True)
    context['calendar'] = mark_safe(html_cal)
    context['prev_month'] = prev_month(d)
    context['next_month'] = next_month(d)
    context['event'] = True
    return render(request, 'event/index.html', context)


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
        return redirect('/event/')
    return render(request, 'event/event.html', {'form': form, 'event':True})

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
    return redirect('/event/')

class EventDeleteView(generic.DeleteView):
    model = Event
    template_name = 'event/event_delete_confirm.html'
    success_url = '/event/'


def checkAjax(request):
    print('request checkAjax ')
    id = request.POST['id']
    stat = request.POST['stat']
    print('param - ', id , stat)
    event = Event.objects.get(id=id)
    event.completed = stat
    event.save()
    list = ['success']
    return JsonResponse(list, safe=False)
