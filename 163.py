import requests
import urllib

r = requests.get('http://music.163.com/api/playlist/detail?id=2884035')  #网易原创歌曲榜
#r = requests.get('http://music.163.com/api/playlist/detail?id=3778678')  #云音乐热歌榜
#r = requests.get('http://music.163.com/api/playlist/detail?id=3779629')  #云音乐新歌榜


arr = r.json()['result']['tracks']

for i in range(10):
    name = str(i+1)+' '+ arr[i]['name']+ '.mp3'
    link = arr[i]['mp3Url']

    urllib.request.urlretrieve(link, '. 163music\\'+name )

    print(name + 'download compplete')

