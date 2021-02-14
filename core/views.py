from django.shortcuts import render
from weathers.utils import weather
from django.utils.safestring import mark_safe
from .utils import get_date, prev_month, next_month
from recommends.utils import recommend
from event.utils import Calendar
# Create your views here.
def index(request):
    context = weather('서울')
    context['recommend'] = recommend(context['weatherInfo']['temp'])

    d = get_date()
    cal = Calendar(d.year, d.month)
    html_cal = cal.formatmonth(withyear=True)
    context['calendar'] = mark_safe(html_cal)
    context['prev_month'] = prev_month(d)
    context['next_month'] = next_month(d)

    return render(request, 'core/index.html', context)