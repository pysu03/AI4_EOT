from django.shortcuts import render
from .utils import weather

def weather_detail(request):
    location = request.GET.get('location', 'seoul')
    context = weather(location)
    context['weather'] = True
    return render(request, 'weather/weather.html', context)