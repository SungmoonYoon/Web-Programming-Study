import urllib, urllib.request, json, csv, codecs, time

matrix = []

inputfilename = 'in5.csv'
outputfilename = 'out55.csv'
savefilename = 'save55.txt' 
savecount = 100  #몇개마다 저장할지에 대한 카운터

f = open(inputfilename, 'r')
csvReader = csv.reader(f)
save = open(savefilename, 'a')
save.write("save process \n")
save.close()
for row in csvReader:
         matrix.append(row)
         
f.close()
start_list = []
dest_list = []

for i in range(0, len(matrix)):
         start_list.append(matrix[i][0:2])
         dest_list.append(matrix[i][2:4])
bucheon = ['부천시 소사구','부천시 오정구','부천시 원미구']
jeju = ("126.5311380", "33.4995680")
ulleng = ("130.9057000", "37.4844510")
suguipo = ("126.5105750", "33.2555920")
hdr = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}
naver_url = "https://m.map.naver.com/routeSearchAjax.nhn?query="
naver_url2 = "https://m.map.naver.com/route.nhn#/drive/list/"
car_url = 'https://m.map.naver.com/spirra/findCarRoute.nhn?route=route3&output=json&coord_type=latlng&search=0&car=0&mileage=12.4'

print(str(len(matrix))+"개의 자료에 대한 파싱을 시작합니다")

for i in range(4800, len(matrix)):
         save = open(savefilename, 'a')
         t1 = time.time()

         if start_list[i][1] in bucheon:
                  strq=urllib.parse.quote(start_list[i][0]+start_list[i][1][0:6]+'동')
         else: 
                  strq = urllib.parse.quote(start_list[i][0]+start_list[i][1])

         if dest_list[i][1] in bucheon:
                  strq2 = urllib.parse.quote(dest_list[i][0]+dest_list[i][1][0:6]+'동')
         else:
                  strq2 = urllib.parse.quote(dest_list[i][0]+dest_list[i][1])

         req = urllib.request.Request(naver_url+strq, headers = hdr)
         req2 = urllib.request.Request(naver_url+strq2, headers = hdr)

         data = urllib.request.urlopen(req).read().decode("utf-8")
         data2 = urllib.request.urlopen(req2).read().decode("utf-8")

         js = json.loads(data)
         js2 = json.loads(data2)

         #출발지 설정

         name_1 = urllib.parse.quote(js['result']['address']['list'][0]['name'])
         x_1 = js['result']['address']['list'][0]['x']
         y_1 = js['result']['address']['list'][0]['y']

         name_2 =  urllib.parse.quote(js2['result']['address']['list'][0]['name'])
         x_2 = js2['result']['address']['list'][0]['x']
         y_2 = js2['result']['address']['list'][0]['y']

         start = '&start='+ x_1 + ',' + y_1 +',' + name_1
         dest = '&destination='+ x_2 + ',' + y_2 +',' + name_2
         parameter = start+dest
         if (name_1,x_1,y_1)==(name_2,x_2,y_2):
                  matrix[i].append("000.000")
         elif (x_2,y_2)==jeju or (x_2,y_2)==ulleng or (x_2,y_2)==suguipo:
                  matrix[i].append("000.000")
         else:
                  req3 = urllib.request.Request(car_url+parameter, headers = hdr)
                  data3 = urllib.request.urlopen(req3).read().decode("utf-8")
             
                  js3 = json.loads(data3)
                  dis = float(js3['summary']['totalDistance'])/1000
                  matrix[i].append(dis)

         t2 = time.time()
         t3 = (t2-t1)
         t3 = round(t3,2)
         
         print(str(i)+'번째 검색에서 걸린 시간 : '+str(t3))
         print(matrix[i])
         save.write(str(i)+'\n')
         save.close()
         if (i%savecount == 0) or (i == len(matrix)-1):
                  o = open(outputfilename,'w')
                  csvWriter = csv.writer(o, delimiter=',')
                  for j in range(4800, i):
                          # csvWriter.writerow(matrix[j])
                          o.write(str(matrix[j][0])+','+str(matrix[j][1])+','+str(matrix[j][2])+','+str(matrix[j][3]) + ',' +str(matrix[j][4])+'\n')
                  o.close()
                  print(str(i)+"번째 까지"+outputfilename+"에 저장합니다.")

save.close()
