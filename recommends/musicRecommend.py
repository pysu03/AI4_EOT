import pandas as pd

def cleanLoadMusic() :
    context = {}
    songRecommend_df = pd.read_csv('recommends/weather_song_data.csv', encoding='CP949')
    # csv파일 불러오기
    songRecommend_df_weather = songRecommend_df.loc[songRecommend_df['weather'].str.contains('맑음')]
    # weather 부분 조건지정
    recommendSong = songRecommend_df_weather[['title', 'artist', 'weather']]
    # 읽고자 하는 부분 선택
    loadClean = recommendSong.sample(n=2, replace=True)
    context['text'] = {loadClean}

def cloudLoadMusic() :
    context = {}
    songRecommend_df = pd.read_csv('recommends/weather_song_data.csv', encoding='CP949')
    songRecommend_df_weather = songRecommend_df.loc[songRecommend_df['weather'].str.contains('흐림')]
    recommendSong = songRecommend_df_weather[['title', 'artist', 'weather']]
    loadCloud = recommendSong.sample(n=2, replace=True)
    context['text'] = {loadCloud}

def snowLoadMusic() :
    context = {}
    songRecommend_df = pd.read_csv('recommends/weather_song_data.csv', encoding='CP949')
    songRecommend_df_weather = songRecommend_df.loc[songRecommend_df['weather'].str.contains('눈')]
    recommendSong = songRecommend_df_weather[['title', 'artist', 'weather']]
    loadSnow = recommendSong.sample(n=2, replace=True)
    context['text'] = {loadSnow}

def rainLoadMusic() :
    context = {}
    songRecommend_df = pd.read_csv('recommends/weather_song_data.csv', encoding='CP949')
    songRecommend_df_weather = songRecommend_df.loc[songRecommend_df['weather'].str.contains('비')]
    recommendSong = songRecommend_df_weather[['title', 'artist', 'weather']]
    loadRain = recommendSong.sample(n=2, replace=True)
    context['text'] = {loadRain}

def hotLoadMusic() :
    context = {}
    songRecommend_df = pd.read_csv('recommends/weather_song_data.csv', encoding='CP949')
    songRecommend_df_weather = songRecommend_df.loc[songRecommend_df['weather'].str.contains('더운')]
    recommendSong = songRecommend_df_weather[['title', 'artist', 'weather']]
    loadHot = recommendSong.sample(n=2, replace=True)
    context['text'] = {loadHot}

def normalLoadMusic() :
    context = {}
    songRecommend_df = pd.read_csv('recommends/weather_song_data.csv', encoding='CP949')
    recommendSong = songRecommend_df[['title', 'artist', 'weather']]
    loadNormal = recommendSong.sample(n=2, replace=True)
    context['text'] = {loadNormal}

