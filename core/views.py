from django.shortcuts import render
from weathers.utils import weather
from django.utils.safestring import mark_safe
from .utils import get_date, prev_month, next_month
from recommends.utils import recommend, recommend_music
from event.utils import Calendar


def index(request):
    location = request.GET.get('location', 'seoul')
    context = weather(location)

    
    context['recommend'] = recommend(context['weatherInfo']['temp'])
    context['recommend_music'] = recommend_music(context['weatherInfo']['temp'], context['weatherInfo']['description'])
     

    user = request.user.id
    print(request.user)
    d = get_date(request.GET.get('month', None))
    cal = Calendar(d.year, d.month)
    html_cal = cal.formatmonth(user, withyear=True)
    context['calendar'] = mark_safe(html_cal)
    context['prev_month'] = prev_month(d)
    context['next_month'] = next_month(d)

    context['home'] = True
    return render(request, 'core/index.html', context)
