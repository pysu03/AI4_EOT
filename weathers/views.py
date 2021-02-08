from django.shortcuts import render, redirect
from django.shortcuts import render
import requests
from datetime import datetime
import time
from geopy.geocoders import Nominatim  # pip install geopy
from pprint import pprint
from .models import Todayweather

# Create your views here.
def index(request):
    return render(request, 'index.html')

def search(requset):
    return render(requset, 'search.html')

def weather(request):
    if request.method == 'POST':
        # Todayweather
        # 위도, 경도 구하기
        location = request.POST['location']
        print('weather location - ' , location)
        app = Nominatim(user_agent='tutorial')
        loc = app.geocode(location)
        location_code = loc.raw
        pprint(loc)
        lat_code = location_code['lat']
        lon_code = location_code['lon']
        # print(lat_code)
        # print(lon_code)

        # openweathermap api로 날씨 데이터 받기
        # user_api = '7757c17e77da5628ba7ddfd9637604f3'
        complete_api_link = 'http://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid=7757c17e77da5628ba7ddfd9637604f3&units=metric'.format(lat_code, lon_code)
        # print(complete_api_link)
        api_link = requests.get(complete_api_link)
        api_data = api_link.json()
        # print(api_data)

        # 미세먼지
        air_pollution_api_link = 'http://api.openweathermap.org/data/2.5/air_pollution?lat={}&lon={}&appid=7757c17e77da5628ba7ddfd9637604f3&units=metric'.format(
            lat_code, lon_code)
        airP_api_link = requests.get(air_pollution_api_link)
        airP_data = airP_api_link.json()
        # print(airP_data)

        # create variables to store and display data
        temp_city = api_data['main']['temp']
        feels_like = api_data['main']['feels_like']
        temp_min = api_data['main']['temp_min']
        temp_max = api_data['main']['temp_max']
        weather_desc = api_data['weather'][0]['description']
        hmdt = api_data['main']['humidity']
        wind_spd = api_data['wind']['speed']
        date_time = datetime.now().strftime("%d %b %y | %I:%M:%S %p")
        sunrise = time.strftime("%H:%M:%S", time.gmtime(api_data['sys']['sunrise'] + 32400))
        sunset = time.strftime("%H:%M:%S", time.gmtime(api_data['sys']['sunset'] + 32400))
        # 미세먼지
        pm2_5 = (airP_data['list'][0]['components']['pm2_5'])
        pm10 = (airP_data['list'][0]['components']['pm10'])

        print("------------------------------------------------------")
        print("Weather Stats for - {} || {}".format(location.upper(), date_time))
        print("------------------------------------------------------")

        print("현재 기온 : {:.2f} °C".format(temp_city))
        print("체감 온도 : {:.2f} °C".format(feels_like))
        print("최저 기온 : {:.2f} °C".format(temp_min))
        print("최고 기온 : {:.2f} °C".format(temp_max))
        print("현재 날씨 :", weather_desc)
        print("현재 습도 :", hmdt, '%')
        print("현재 풍속 :", wind_spd, 'km/h')
        print("일출 시간 :", sunrise)
        print("일몰 시간 :", sunset)
        print("초미세먼지:", pm2_5, '㎍/m³')
        print("미세 먼지 :", pm10, '㎍/m³')

        # DB에 저장
        # get_todayweather = Todayweather(
        #     location     = loc,
        #     temp         = api_data['main']['temp'],
        #     feels_like   = api_data['main']['feels_like'],
        #     temp_min     = api_data['main']['temp_min'],
        #     temp_max     = api_data['main']['temp_max'],
        #     weather_desc = api_data['weather'][0]['description'],
        #     hmdt         = api_data['main']['humidity'],
        #     wind_spd     = api_data['wind']['speed'],
        #     date_time    = datetime.now().strftime("%d %b %y | %I:%M:%S %p"),
        #     sunrise      = time.strftime("%H:%M:%S", time.gmtime(api_data['sys']['sunrise'] + 32400)),
        #     sunset       = time.strftime("%H:%M:%S", time.gmtime(api_data['sys']['sunset'] + 32400)),
        #     pm2_5        = airP_data['list'][0]['components']['pm2_5'],
        #     pm10         = airP_data['list'][0]['components']['pm10']
        # )
        # get_todayweather.save()

        # weather.html에 출력
        context = {}
        context['location']     = location_code['display_name'].split(',')[0]
        context['temp']         = api_data['main']['temp']
        context['feels_like']   = api_data['main']['feels_like']
        context['temp_min']     = api_data['main']['temp_min']
        context['temp_max']     = api_data['main']['temp_max']
        context['weather_desc'] = api_data['weather'][0]['description']
        context['hmdt']         = api_data['main']['humidity']
        context['wind_spd']     = api_data['wind']['speed']
        context['date_time']    = datetime.now().strftime("%d %b %y | %I:%M:%S %p")
        context['sunrise']      = time.strftime("%H:%M:%S", time.gmtime(api_data['sys']['sunrise'] + 32400))
        context['sunset']       = time.strftime("%H:%M:%S", time.gmtime(api_data['sys']['sunset'] + 32400))
        context['pm2_5']        = airP_data['list'][0]['components']['pm2_5']
        context['pm10']         = airP_data['list'][0]['components']['pm10']

    return render(request, 'weather.html', context)
