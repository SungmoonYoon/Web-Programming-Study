import urllib, urllib.request, json, csv, codecs, time

a = input("출발지 검색어 :")
b = input('도착지 검색어 :')
hdr = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}
naver_url = "https://m.map.naver.com/routeSearchAjax.nhn?query="
naver_url2 = "https://m.map.naver.com/route.nhn#/drive/list/"
car_url = 'https://m.map.naver.com/spirra/findCarRoute.nhn?route=route3&output=json&coord_type=latlng&search=0&car=0&mileage=12.4'


strq = urllib.parse.quote(a)
strq2 = urllib.parse.quote(b)
req = urllib.request.Request(naver_url+strq, headers = hdr)
req2 = urllib.request.Request(naver_url+strq2, headers = hdr)

data = urllib.request.urlopen(req).read().decode("utf-8")
data2 = urllib.request.urlopen(req2).read().decode("utf-8")

js = json.loads(data)
js2 = json.loads(data2)


name_1 = urllib.parse.quote(js['result']['address']['list'][0]['name'])
x_1 = js['result']['address']['list'][0]['x']
y_1 = js['result']['address']['list'][0]['y']

name_2 =  urllib.parse.quote(js2['result']['address']['list'][0]['name'])
x_2 = js2['result']['address']['list'][0]['x']
y_2 = js2['result']['address']['list'][0]['y']

start = '&start='+ x_1 + ',' + y_1 +',' + name_1
dest = '&destination='+ x_2 + ',' + y_2 +',' + name_2
parameter = start+dest
         
req3 = urllib.request.Request(car_url+parameter, headers = hdr)
data3 = urllib.request.urlopen(req3).read().decode("utf-8")
             
js3 = json.loads(data3)
dis = float(js3['summary']['totalDistance'])/1000

print(dis)
