# import requests
# from bs4 import BeautifulSoup
#
# if __name__ == "__main__":
#     RANK = 10
#
#     header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko'}
#     req = requests.get('https://www.melon.com/chart/index.htm', headers=header)
#     html = req.text
#     parse = BeautifulSoup(html, 'html.parser')
#
#     titles = parse.find_all("div", {"class": "ellipsis rank01"})
#     songs = parse.find_all("div", {"class": "ellipsis rank02"})
#
#     title = []
#     song = []
#
#     for t in titles:
#         title.append(t.find('a').text)
#
#     for s in songs:
#         song.append(s.find('span', {"class": "checkEllipsis"}).text)
#
#     for i in range(RANK):
#         print('%3d위: %s - %s' % (i + 1, title[i], song[i]))

import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup
import urllib.parse


# 멜론 DJ플레이리스트 검색 후 검색 결과
baseUrl = 'https://www.melon.com/search/dj/index.htm?q='
plusUrl = input('검색어를 입력하세요 : ')
lastUrl = '&section=&searchGnbYn=Y&kkoSpl=Y&kkoDpType=&linkOrText=T&ipath=srch_form'

# 검색 자동 변환 (url 구성)
url = baseUrl + urllib.parse.quote_plus(plusUrl) + lastUrl
print(url)

html = requests.get(url)
soup = BeautifulSoup(html.text, 'html.parser')
print(soup)

musicList = soup.find_all("a")
print(len(musicList))


# html = urlopen(url)
# bsObject = bs(html, "html.parser")
# html = urlopen(url)
# parse = BeautifulSoup(html, 'html.parser')
# 조건에 맞는 파일을 다 출력해라
# title = bsObject.find_all(class_='dj_collection_info')
# print(type(title))
#
# titles = parse.find_all("div", {"class": "dj_collection_info"})
# songs = parse.find_all("div", {"class": "ellipsis rank02"})
#
# for i in titles:
#     print(i.attrs['title'])
#     print(i.attrs['href'])
#     print()

