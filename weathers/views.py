from django.shortcuts import render
from .utils import weather

def weather_detail(request):
    location="seoul"
    context = weather(location)
    return render(request, 'weather/weather.html', context)