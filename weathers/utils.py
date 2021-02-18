
import requests
from datetime import datetime
import time
from geopy.geocoders import Nominatim
from pprint import pprint
from .models import Todayweather

APIKEY = '7757c17e77da5628ba7ddfd9637604f3'
WEAHTER = 'weather'
AIR = 'air_pollution'
FORCAST = 'forecast'
ONEDAY = 'onecall'

def getLatAndLon(location): # 위도 경도
    app = Nominatim(user_agent='tutorial')
    loc = app.geocode(location)
    location_code = loc.raw
    location_name = location_code['display_name'].split(',')[0]
    return (location_name, location_code['lat'], location_code['lon'])

def getApiData(apiType, lat_code, lon_code):
    apiURL = 'http://api.openweathermap.org/data/2.5/{}?lat={}&lon={}&appid={}&units=metric'.format(apiType, lat_code, lon_code, APIKEY)
    apiData = requests.get(apiURL).json()
    return apiData

def getWeatherData(lat_code, lon_code):
    weatherData = getApiData(WEAHTER, lat_code, lon_code)

    # 기온, 체감온도, 최저기온, 최고기온, 날씨상태, 습도, 풍속, 일출, 일몰, 현재시간
    context = {}
    context['temp'] = weatherData['main']['temp']
    context['feels_like'] = weatherData['main']['feels_like']
    context['temp_min'] = weatherData['main']['temp_min']
    context['temp_max'] = weatherData['main']['temp_max']
    context['weather_desc'] = weatherData['weather'][0]['description']
    context['hmdt'] = weatherData['main']['humidity']
    context['wind_spd'] = weatherData['wind']['speed']
    context['icon']     = weatherData['weather'][0]['icon']
    context['main'] = weatherData['weather'][0]['main']
    context['description'] = weatherData['weather'][0]['description']
    context['sunrise'] = time.strftime("%H:%M:%S", time.gmtime(weatherData['sys']['sunrise'] + 32400))
    context['sunset'] = time.strftime("%H:%M:%S", time.gmtime(weatherData['sys']['sunset'] + 32400))

    return context

def getAirData(lat_code, lon_code):
    airData = getApiData(AIR, lat_code, lon_code)

    # 미세먼지, 초미세먼지
    context= {}
    context['pm2_5'] = airData['list'][0]['components']['pm2_5']
    context['pm10'] = airData['list'][0]['components']['pm10']
    return context

def getForecastData(lat_code, lon_code):
    ForcastData = getApiData(FORCAST, lat_code, lon_code)

    # create variables to store and display data
    # 갱신 시간, 기온, 강수확률 리스트에 담기
    list_data_time = []     # 차트 categories에 넣을 리스트
    list_data_temp = []     # 차트에 넣을 기온 리스트
    list_data_pop = []      # 차트에 넣을 강수확률 리스트
    list_data_time_temp = []

    now = datetime.now()
    for i in range(16):
        tmp = ForcastData['list'][i]['dt_txt']
        tmp = datetime.strptime(tmp,'%Y-%m-%d %H:%M:%S')
        list_data_time_temp.append(tmp)
        list_data_time.append(ForcastData['list'][i]['dt_txt'][11:13] + '시')
        list_data_temp.append(ForcastData['list'][i]['main']['temp']) # 현재 기온
        list_data_pop.append(ForcastData['list'][i]['pop']) # 강수 확률

    # 차트에 넣을 데이터
    # 현재 시간에서 다음으로 갱신되는 시간부터 8개 데이터 뽑기
    list_fore24_time = []
    list_fore24_temp = []
    list_fore24_pop = []

    for i, v in enumerate(list_data_time_temp):
        if now < v:
            list_fore24_time = list_data_time[i:i+8]
            list_fore24_temp = list_data_temp[i:i+8]
            list_fore24_pop = list_data_pop[i:i+8]
            break
    list_fore24_pop=[round(x*100, 1) for x in list_fore24_pop]
 
    return list_fore24_time, list_fore24_pop, list_fore24_temp


def getOneDayData(lat_code, lon_code):
    OneDayData = getApiData(ONEDAY, lat_code, lon_code)

    # 하루 단위 날씨    

    context= {}
    temp_main = []
    time_main = []
    for i in range(0,7):
        tmp1 = 'd_'+str(i)
        tmp2 = 'd_'+str(i)+'_temp_m'
        tmp3 = 'd_'+str(i)+'_temp_M'
        tmp4 = 'd_'+str(i)+'_temp_i'
        tmp5 = 'd_'+str(i)+'_temp_s'
        time_main.append(time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(OneDayData['hourly'][0]['dt'] + 32400))[11:13] + '시')
        temp_main.append(OneDayData['hourly'][i]['temp'])
        context[tmp1] = time.strftime("%m/%d", time.gmtime(OneDayData['daily'][i]['dt'] + 32400))
        context[tmp2] = round(OneDayData['daily'][i]['temp']['min'], 1)
        context[tmp3] = round(OneDayData['daily'][i]['temp']['max'], 1)
        context[tmp4] = OneDayData['daily'][i]['weather'][0]['icon']
        context[tmp5] = OneDayData['daily'][i]['weather'][0]['main']

    context['temp_main'] = temp_main
    context['time_main'] = time_main
    context['data1_pop'] = round(OneDayData['hourly'][0]['pop'] * 100)
    return context


def makeContext(location):
    location_name, lat_code, lon_code = getLatAndLon(location) 
    weatherInfo = {}
    context = {}
    weatherInfo['location'] = location_name
    weatherInfo['date_time'] = datetime.now().strftime("%d %b %y | %I:%M:%S %p")
    weatherInfo.update(getWeatherData(lat_code, lon_code))
    weatherInfo.update(getAirData(lat_code, lon_code))
    context['weatherInfo'] = weatherInfo
    context['list_fore24_time'], context['list_fore24_pop'], context['list_fore24_temp'] = getForecastData(lat_code, lon_code)
    context['foreInfo'] = getOneDayData(lat_code, lon_code)
    return context


def weather(location):
    context = makeContext(location)

    return context

