from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.views import generic

from .forms import EventForm
from .models import Event
from .utils import Calendar
from core.utils import get_date, prev_month, next_month

class CalendarView(LoginRequiredMixin, generic.ListView):
    login_url = 'signin'
    redirect_field_name = 'next'
    model = Event
    template_name = 'event/calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get('month', None))
        cal = Calendar(d.year, d.month)
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        return context

@login_required(login_url='signin')
def create_event(request):
    form = EventForm(request.POST or None)
    if request.POST and form.is_valid():
        title = form.cleaned_data['title']
        description = form.cleaned_data['description']
        time = form.cleaned_data['time']
        address = form.cleaned_data['address']
        completed = form.cleaned_data['completed']
        # end_time = form.cleaned_data['end_time']
        Event.objects.get_or_create(
            user=request.user,
            title=title,
            description=description,
            time=time,
            address=address,
            completed=completed,
            # end_time=end_time
        )
        return HttpResponseRedirect(reverse('calendar'))
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
    print('request saveNback - ')
    id = request.POST['id']
    saveCB = request.POST['saveCB']
    print('param - ' , id, saveCB)
    event = Event.objects.get(id=id)
    event.completed = saveCB
    event.save()
    return HttpResponseRedirect(reverse('calendar'))