import calendar
from datetime import date, datetime, timedelta

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

# @login_required(login_url='signin')
# def index(request):
#     return HttpResponse('hello')

def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()

def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month

def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month

class CalendarView(LoginRequiredMixin, generic.ListView):
    login_url = 'signin'
    # redirect_field_name = 'next'
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
        start_time = form.cleaned_data['start_time']
        Event.objects.get_or_create(
            user=request.user,
            title=title,
            description=description,
            start_time=start_time,
        )
        return HttpResponseRedirect(reverse('calendar'))
    return render(request, 'event/event.html', {'form': form})

class EventEdit(generic.UpdateView):
    model = Event
    fields = ['title', 'description', 'start_time']
    template_name = 'event/event.html'

@login_required(login_url='signin')
def event_details(request, event_id):
    event = Event.objects.get(id=event_id)
    context = {
        'event': event
    }
    return render(request, 'event/event_details.html', context)