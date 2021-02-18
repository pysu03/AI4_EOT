import os
import pandas as pd
from django.conf import settings

def recommend(data):
    currentTemp = data
    winter = currentTemp <= 5
    earlyWinter = currentTemp >=5 and currentTemp < 9
    beginWinter = currentTemp >= 9 and currentTemp < 12
    fall = currentTemp >= 12 and currentTemp < 17
    earlyFall = currentTemp >= 17 and currentTemp < 20
    earlySummer = currentTemp >= 20 and currentTemp < 23
    beginSummer = currentTemp >= 23 and currentTemp < 28
    summer = currentTemp >= 28

    context = {}
    if winter :
        context['text'] = ['패딩', '두꺼운 코트', '누빔 옷', '기모', '목도리']
        context['filename'] = "winter1.png"
    elif earlyWinter :
        context['text'] = ['울코트', '히트텍', '가죽 옷', '기모']
        context['filename'] = "earlywinter1.png"
    elif beginWinter :
        context['text'] = ['트렌치 코트', '야상', '점프', '스타킹', '기모바지']
        context['filename'] = "beginwinter1.png"        
    elif fall :
        context['text'] = ['자켓', '가디건', '청자켓', '니트', '스타킹', '청바지']
        context['filename'] = "fall1.png"
    elif earlyFall :
        context['text'] = ['얇은 가디건', '니트', '맨투맨', '후드', '긴바지']
        context['filename'] = "earlyfall1.png"
    elif earlySummer :
        context['text'] = ['블라우스', '긴팔 티', '면바지', '슬랙스']
        context['filename'] = "earlysummer1.png"
    elif beginSummer :
        context['text'] = ['반팔', '얇은 셔츠', '반바지', '면바지']
        context['filename'] = "beginsummer1.png"
    elif summer :
        context['text'] = ['민소매', '반팔', '반바지', '짧은 치마', '린넨 옷']
        context['filename'] = "summer1.png"

    return context


def weatherLoadMusic(weatherType):
    fileName = os.path.join(settings.BASE_DIR, 'static/data/weather_song_data.csv')
    songRecommend_df = pd.read_csv(fileName, encoding='CP949')
    songRecommend_df_weather = songRecommend_df.loc[songRecommend_df['weather'].str.contains(weatherType)]
    recommendSong = songRecommend_df_weather[['title', 'artist', 'weather']]
    loadClean = recommendSong.sample(n=2, replace=True)
    musicdata = loadClean.values.tolist()
    return musicdata

def normalLoadMusic() :
    fileName = os.path.join(settings.BASE_DIR, 'static/data/weather_song_data.csv')
    songRecommend_df = pd.read_csv(fileName, encoding='CP949')
    recommendSong = songRecommend_df[['title', 'artist']]
    loadClean = recommendSong.sample(n=2, replace=True)
    musicdata = loadClean.values.tolist()
    return musicdata


def recommend_music(temp, description):
    currentTemp = temp
    currentIcon = description
    clean = "clean"
    rain = "rain"
    snow = "snow"
    cloud = "clouds"

    if currentTemp >= 28 :
        musics = weatherLoadMusic('더운')
    elif currentIcon.find(clean) != -1:
        musics = weatherLoadMusic('맑음')
    elif currentIcon.find(rain) != -1 :
        musics = weatherLoadMusic('비')
    elif currentIcon.find(snow) != -1:
        musics = weatherLoadMusic('눈')
    elif currentIcon.find(cloud) != -1 :
        musics = weatherLoadMusic('흐림')
    else :
        musics = normalLoadMusic()

    musicdata = [' - '.join(x) for x in musics]
    return musicdata