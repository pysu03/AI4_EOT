from django.shortcuts import render, redirect
import requests
from datetime import datetime
import time
from geopy.geocoders import Nominatim  
from .models import Todayweather

# Create your views here.
def search(requset):
    return render(requset, 'search.html')

def weather(request):
    if request.method == 'POST':
        
        # 위도, 경도
        location = request.POST['location']
        app = Nominatim(user_agent='tutorial')
        loc = app.geocode(location)
        location_code = loc.raw
        lat_code = location_code['lat']
        lon_code = location_code['lon']

        # openweathermap API
        # user_api = '7757c17e77da5628ba7ddfd9637604f3'

        complete_api_link = 'http://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid=7757c17e77da5628ba7ddfd9637604f3&units=metric'.format(lat_code, lon_code)
        api_link = requests.get(complete_api_link)
        api_data = api_link.json()

        # 미세먼지 API
        air_pollution_api_link = 'http://api.openweathermap.org/data/2.5/air_pollution?lat={}&lon={}&appid=7757c17e77da5628ba7ddfd9637604f3&units=metric'.format(lat_code, lon_code)
        airP_api_link = requests.get(air_pollution_api_link)
        airP_data = airP_api_link.json()
        # print(airP_data)

        # create variables to store and display data

        # 기온, 체감온도, 최저기온, 최고기온, 날씨상태, 습도, 풍속, 일출, 일몰, 현재시간

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

        # 미세먼지, 초미셈먼지
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

        # Forecast
        # openweathermap api로 날씨 데이터 받기
        # user_api = '7757c17e77da5628ba7ddfd9637604f3'
        fore_complete_api_link = 'http://api.openweathermap.org/data/2.5/forecast?lat={}&lon={}&appid=7757c17e77da5628ba7ddfd9637604f3&units=metric'.format(
            lat_code, lon_code)
        # print(fore_complete_api_link)
        fore_api_link = requests.get(fore_complete_api_link)
        fore_data = fore_api_link.json()
        # print(fore_data)

        # create variables to store and display data
        # 갱신 시간, 기온, 강수확률 리스트에 담기
        list_data_time = []     # 차트 categories에 넣을 리스트
        list_data_temp = []     # 차트에 넣을 기온 리스트
        list_data_pop = []      # 차트에 넣을 강수확률 리스트
        print("------------------------------------------------------")
        data1 = fore_data['list'][0]['dt_txt']
        data1_time = fore_data['list'][0]['dt_txt'][11:13] + '시'
        data1_temp = fore_data['list'][0]['main']['temp']
        data1_pop = fore_data['list'][0]['pop']
        list_data_time.append(data1_time)
        list_data_temp.append(data1_temp)
        list_data_pop.append(data1_pop)
        print(data1)
        print("현재 기온 : {:.2f} °C".format(data1_temp))
        print("강수 확률 :", data1_pop, '%')
        print("------------------------------------------------------")
        data2 = fore_data['list'][1]['dt_txt']
        data2_time = fore_data['list'][1]['dt_txt'][11:13] + '시'
        data2_temp = fore_data['list'][1]['main']['temp']
        data2_pop = fore_data['list'][1]['pop']
        list_data_time.append(data2_time)
        list_data_temp.append(data2_temp)
        list_data_pop.append(data2_pop)
        print(data2)
        print("현재 기온 : {:.2f} °C".format(data2_temp))
        print("강수 확률 :", data2_pop, '%')
        print("------------------------------------------------------")
        data3 = fore_data['list'][2]['dt_txt']
        data3_time = fore_data['list'][2]['dt_txt'][11:13] + '시'
        data3_temp = fore_data['list'][2]['main']['temp']
        data3_pop = fore_data['list'][2]['pop']
        list_data_time.append(data3_time)
        list_data_temp.append(data3_temp)
        list_data_pop.append(data3_pop)
        print(data3)
        print("현재 기온 : {:.2f} °C".format(data3_temp))
        print("강수 확률 :", data3_pop, '%')
        print("------------------------------------------------------")
        data4 = fore_data['list'][3]['dt_txt']
        data4_time = fore_data['list'][3]['dt_txt'][11:13] + '시'
        data4_temp = fore_data['list'][3]['main']['temp']
        data4_pop = fore_data['list'][3]['pop']
        list_data_time.append(data4_time)
        list_data_temp.append(data4_temp)
        list_data_pop.append(data4_pop)
        print(data4)
        print("현재 기온 : {:.2f} °C".format(data4_temp))
        print("강수 확률 :", data4_pop, '%')
        print("------------------------------------------------------")
        data5 = fore_data['list'][4]['dt_txt']
        data5_time = fore_data['list'][4]['dt_txt'][11:13] + '시'
        data5_temp = fore_data['list'][4]['main']['temp']
        data5_pop = fore_data['list'][4]['pop']
        list_data_time.append(data5_time)
        list_data_temp.append(data5_temp)
        list_data_pop.append(data5_pop)
        print(data5)
        print("현재 기온 : {:.2f} °C".format(data5_temp))
        print("강수 확률 :", data5_pop, '%')
        print("------------------------------------------------------")
        data6 = fore_data['list'][5]['dt_txt']
        data6_time = fore_data['list'][5]['dt_txt'][11:13] + '시'
        data6_temp = fore_data['list'][5]['main']['temp']
        data6_pop = fore_data['list'][5]['pop']
        list_data_time.append(data6_time)
        list_data_temp.append(data6_temp)
        list_data_pop.append(data6_pop)
        print(data6)
        print("현재 기온 : {:.2f} °C".format(data6_temp))
        print("강수 확률 :", data6_pop, '%')
        print("------------------------------------------------------")
        data7 = fore_data['list'][6]['dt_txt']
        data7_time = fore_data['list'][6]['dt_txt'][11:13] + '시'
        data7_temp = fore_data['list'][6]['main']['temp']
        data7_pop = fore_data['list'][6]['pop']
        list_data_time.append(data7_time)
        list_data_temp.append(data7_temp)
        list_data_pop.append(data7_pop)
        print(data7)
        print("현재 기온 : {:.2f} °C".format(data7_temp))
        print("강수 확률 :", data7_pop, '%')
        print("------------------------------------------------------")
        data8 = fore_data['list'][7]['dt_txt']
        data8_time = fore_data['list'][7]['dt_txt'][11:13] + '시'
        data8_temp = fore_data['list'][7]['main']['temp']
        data8_pop = fore_data['list'][7]['pop']
        list_data_time.append(data8_time)
        list_data_temp.append(data8_temp)
        list_data_pop.append(data8_pop)
        print(data8)
        print("현재 기온 : {:.2f} °C".format(data8_temp))
        print("강수 확률 :", data8_pop, '%')
        print("------------------------------------------------------")
        data9 = fore_data['list'][8]['dt_txt']
        data9_time = fore_data['list'][8]['dt_txt'][11:13] + '시'
        data9_temp = fore_data['list'][8]['main']['temp']
        data9_pop = fore_data['list'][8]['pop']
        list_data_time.append(data9_time)
        list_data_temp.append(data9_temp)
        list_data_pop.append(data9_pop)
        print(data9)
        print("현재 기온 : {:.2f} °C".format(data9_temp))
        print("강수 확률 :", data9_pop, '%')
        print("------------------------------------------------------")
        data10 = fore_data['list'][9]['dt_txt']
        data10_time = fore_data['list'][9]['dt_txt'][11:13] + '시'
        data10_temp = fore_data['list'][9]['main']['temp']
        data10_pop = fore_data['list'][9]['pop']
        list_data_time.append(data10_time)
        list_data_temp.append(data10_temp)
        list_data_pop.append(data10_pop)
        print(data10)
        print("현재 기온 : {:.2f} °C".format(data10_temp))
        print("강수 확률 :", data10_pop, '%')
        print("------------------------------------------------------")
        data11 = fore_data['list'][10]['dt_txt']
        data11_time = fore_data['list'][10]['dt_txt'][11:13] + '시'
        data11_temp = fore_data['list'][10]['main']['temp']
        data11_pop = fore_data['list'][10]['pop']
        list_data_time.append(data11_time)
        list_data_temp.append(data11_temp)
        list_data_pop.append(data11_pop)
        print(data11)
        print("현재 기온 : {:.2f} °C".format(data11_temp))
        print("강수 확률 :", data11_pop, '%')
        print("------------------------------------------------------")
        data12 = fore_data['list'][11]['dt_txt']
        data12_time = fore_data['list'][11]['dt_txt'][11:13] + '시'
        data12_temp = fore_data['list'][11]['main']['temp']
        data12_pop = fore_data['list'][11]['pop']
        list_data_time.append(data12_time)
        list_data_temp.append(data12_temp)
        list_data_pop.append(data12_pop)
        print(data12)
        print("현재 기온 : {:.2f} °C".format(data12_temp))
        print("강수 확률 :", data12_pop, '%')
        print("------------------------------------------------------")
        data13 = fore_data['list'][12]['dt_txt']
        data13_time = fore_data['list'][12]['dt_txt'][11:13] + '시'
        data13_temp = fore_data['list'][12]['main']['temp']
        data13_pop = fore_data['list'][12]['pop']
        list_data_time.append(data13_time)
        list_data_temp.append(data13_temp)
        list_data_pop.append(data13_pop)
        print(data13)
        print("현재 기온 : {:.2f} °C".format(data13_temp))
        print("강수 확률 :", data13_pop, '%')
        print("------------------------------------------------------")
        data14 = fore_data['list'][13]['dt_txt']
        data14_time = fore_data['list'][13]['dt_txt'][11:13] + '시'
        data14_temp = fore_data['list'][13]['main']['temp']
        data14_pop = fore_data['list'][13]['pop']
        list_data_time.append(data14_time)
        list_data_temp.append(data14_temp)
        list_data_pop.append(data14_pop)
        print(data14)
        print("현재 기온 : {:.2f} °C".format(data14_temp))
        print("강수 확률 :", data14_pop, '%')
        print("------------------------------------------------------")
        data15 = fore_data['list'][14]['dt_txt']
        data15_time = fore_data['list'][14]['dt_txt'][11:13] + '시'
        data15_temp = fore_data['list'][14]['main']['temp']
        data15_pop = fore_data['list'][14]['pop']
        list_data_time.append(data15_time)
        list_data_temp.append(data15_temp)
        list_data_pop.append(data15_pop)
        print(data15)
        print("현재 기온 : {:.2f} °C".format(data15_temp))
        print("강수 확률 :", data15_pop, '%')
        print("------------------------------------------------------")
        data16 = fore_data['list'][15]['dt_txt']
        data16_time = fore_data['list'][15]['dt_txt'][11:13] + '시'
        data16_temp = fore_data['list'][15]['main']['temp']
        data16_pop = fore_data['list'][15]['pop']
        list_data_time.append(data16_time)
        list_data_temp.append(data16_temp)
        list_data_pop.append(data16_pop)
        print(data16)
        print("현재 기온 : {:.2f} °C".format(data16_temp))
        print("강수 확률 :", data16_pop, '%')
        # print(list_data_time)
        # print(list_data_temp)
        # print(list_data_pop)


        # 문자열 >> 시간
        now = datetime.now()
        # print(now)
        date1_t = datetime.strptime(data1, '%Y-%m-%d %H:%M:%S')
        date2_t = datetime.strptime(data2, '%Y-%m-%d %H:%M:%S')
        date3_t = datetime.strptime(data3, '%Y-%m-%d %H:%M:%S')
        date4_t = datetime.strptime(data4, '%Y-%m-%d %H:%M:%S')
        date5_t = datetime.strptime(data5, '%Y-%m-%d %H:%M:%S')
        date6_t = datetime.strptime(data6, '%Y-%m-%d %H:%M:%S')
        date7_t = datetime.strptime(data7, '%Y-%m-%d %H:%M:%S')
        date8_t = datetime.strptime(data8, '%Y-%m-%d %H:%M:%S')

        # 차트에 넣을 데이터
        # 현재 시간에서 다음으로 갱신되는 시간부터 8개 데이터 뽑기
        list_fore24_time = []
        list_fore24_temp = []
        list_fore24_pop = []
        if now < date1_t:
            print(date1_t, 1)
            list_fore24_time = list_data_time[0:8]
            list_fore24_temp = list_data_temp[0:8]
            list_fore24_pop = list_data_pop[0:8]

        elif now < date2_t:
            print(date2_t, 2)
            list_fore24_time = list_data_time[1:9]
            list_fore24_temp = list_data_temp[1:9]
            list_fore24_pop = list_data_pop[1:9]

        elif now < date3_t:
            print(date3_t, 3)
            list_fore24_time = list_data_time[2:10]
            list_fore24_temp = list_data_temp[2:10]
            list_fore24_pop = list_data_pop[2:10]

        elif now < date4_t:
            print(date4_t, 4)
            list_fore24_time = list_data_time[3:11]
            list_fore24_temp = list_data_temp[3:11]
            list_fore24_pop = list_data_pop[3:11]

        elif now < date5_t:
            print(date5_t, 5)
            list_fore24_time = list_data_time[4:12]
            list_fore24_temp = list_data_temp[4:12]
            list_fore24_pop = list_data_pop[4:12]

        elif now < date6_t:
            print(date6_t, 6)
            list_fore24_time = list_data_time[5:13]
            list_fore24_temp = list_data_temp[5:13]
            list_fore24_pop = list_data_pop[5:13]

        elif now < date7_t:
            print(date7_t, 7)
            list_fore24_time = list_data_time[6:14]
            list_fore24_temp = list_data_temp[6:14]
            list_fore24_pop = list_data_pop[6:14]

        elif now < date8_t:
            print(date8_t, 8)
            list_fore24_time = list_data_time[7:15]
            list_fore24_temp = list_data_temp[7:15]
            list_fore24_pop = list_data_pop[7:15]
        else:
            pass
        print(list_fore24_time)
        print(list_fore24_temp)
        print(list_fore24_pop)

        context2 = {'list_fore24_time': list_fore24_time, 'list_fore24_pop': list_fore24_pop,
                   'list_fore24_temp': list_fore24_temp ,
                    'weatherInfo':context}
        # context를 둘다 스크립트에서 쓰이면 에러 날 수 있음, 다른 작업을 해주면 괜찮음.
    return render(request, 'weather.html', context2)
