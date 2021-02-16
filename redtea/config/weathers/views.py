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
        # 위도, 경도 구하기
        location = request.POST['location']
        print('weather location - ' , location)
        app = Nominatim(user_agent='tutorial')
        loc = app.geocode(location)
        location_code = loc.raw
        pprint(loc)
        lat_code = location_code['lat']
        lon_code = location_code['lon']

        now_data   = func1(location, location_code, lat_code, lon_code)
        chart_data = func2(lat_code, lon_code)

        context = {'temp_main':now_data, 'chart_data':chart_data}

    return render(request, 'weather.html', context)

def func1(location, location_code, lat_code, lon_code):
    # Todayweather
    # openweathermap api로 날씨 데이터 받기
    # user_api = '7757c17e77da5628ba7ddfd9637604f3'
    complete_api_link = 'http://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid=7757c17e77da5628ba7ddfd9637604f3&units=metric&lang=kr'.format(
        lat_code, lon_code)
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
    weather_main = api_data['weather'][0]['main']
    date_time = datetime.now().strftime("%Y-%m-%d | %I:%M:%S %p")
    # 미세먼지
    pm10 = (airP_data['list'][0]['components']['pm10'])
    print("------------------------------------------------------")
    print("Weather Stats for - {} || {}".format(location.upper(), date_time))
    print("------------------------------------------------------")
    print("현재 기온 : {:.2f} °C".format(temp_city))
    print("체감 온도 : {:.2f} °C".format(feels_like))
    print("현재 날씨 :", weather_main)
    print("미세 먼지 :", pm10, '㎍/m³')

    # weather.html에 출력
    context = {}
    context['date_time'] = datetime.now().strftime("%Y-%m-%d | %I:%M:%S %p")
    context['location'] = location_code['display_name'].split(',')[0]
    context['temp'] = round(api_data['main']['temp'],1)
    context['feels_like'] = round(api_data['main']['feels_like'],1)
    context['weather_main'] = api_data['weather'][0]['main']
    context['pm10'] = airP_data['list'][0]['components']['pm10']

    return context

def func2(lat_code, lon_code):
    # openweathermap api로 날씨 데이터 받기
    # user_api = '7757c17e77da5628ba7ddfd9637604f3'
    fore_daily_api_link = 'http://api.openweathermap.org/data/2.5/onecall?lat={}&lon={}&exclude=alerts&appid=7757c17e77da5628ba7ddfd9637604f3&units=metric&lang=kr'.format(
        lat_code, lon_code)
    # print(fore_daily_api_link)
    fore_daily_api_link = requests.get(fore_daily_api_link)
    fore_daily_data = fore_daily_api_link.json()
    # print(fore_daily_data)

    # create variables to store and display data
    temp_main = []
    time_main = []
    print("------------------------------------------------------")
    data1 = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(fore_daily_data['hourly'][0]['dt'] + 32400))
    data1_time = data1[11:13] + '시'
    data1_temp = fore_daily_data['hourly'][0]['temp']
    data1_pop = round(fore_daily_data['hourly'][0]['pop'] * 100)
    print(data1)
    print(data1_time)
    print("기온 : {:.2f} °C".format(data1_temp))
    print("강수 확률 : {} %".format(data1_pop))
    print("------------------------------------------------------")
    data2 = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(fore_daily_data['hourly'][1]['dt'] + 32400))
    data2_time = data2[11:13] + '시'
    data2_temp = fore_daily_data['hourly'][1]['temp']
    time_main.append(data2_time)
    temp_main.append(data2_temp)
    print(data2)
    print("기온 : {:.2f} °C".format(data2_temp))
    print("------------------------------------------------------")
    data3 = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(fore_daily_data['hourly'][2]['dt'] + 32400))
    data3_time = data3[11:13] + '시'
    data3_temp = fore_daily_data['hourly'][2]['temp']
    time_main.append(data3_time)
    temp_main.append(data3_temp)
    print(data3)
    print("기온 : {:.2f} °C".format(data3_temp))
    print("------------------------------------------------------")
    data4 = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(fore_daily_data['hourly'][3]['dt'] + 32400))
    data4_time = data4[11:13] + '시'
    data4_temp = fore_daily_data['hourly'][3]['temp']
    time_main.append(data4_time)
    temp_main.append(data4_temp)
    print(data4)
    print("기온 : {:.2f} °C".format(data4_temp))
    print("------------------------------------------------------")
    data5 = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(fore_daily_data['hourly'][4]['dt'] + 32400))
    data5_time = data5[11:13] + '시'
    data5_temp = fore_daily_data['hourly'][4]['temp']
    time_main.append(data5_time)
    temp_main.append(data5_temp)
    print(data5)
    print("기온 : {:.2f} °C".format(data5_temp))
    print("------------------------------------------------------")
    data6 = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(fore_daily_data['hourly'][5]['dt'] + 32400))
    data6_time = data6[11:13] + '시'
    data6_temp = fore_daily_data['hourly'][5]['temp']
    time_main.append(data6_time)
    temp_main.append(data6_temp)
    print(data6)
    print("기온 : {:.2f} °C".format(data6_temp))
    print("------------------------------------------------------")
    data7 = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(fore_daily_data['hourly'][6]['dt'] + 32400))
    data7_time = data7[11:13] + '시'
    data7_temp = fore_daily_data['hourly'][6]['temp']
    time_main.append(data7_time)
    temp_main.append(data7_temp)
    print(data7)
    print("기온 : {:.2f} °C".format(data7_temp))
    print("------------------------------------------------------")
    print(temp_main)
    print(time_main)
    context = {'temp_main': temp_main, 'time_main': time_main, 'data1_pop': data1_pop}

    return context