# -*- coding:utf-8 -*-
import urllib, urllib2, re, sys
from bs4 import BeautifulSoup
def pri(lst2):
        for i in lst2:
                print i
                
while(1):
        inchar = raw_input("\n 무슨 글자로 시작하는 단어를 찾을까요? \n")
        param = unicode(inchar,'mbcs').encode("utf8")
        url="http://m.krdic.naver.com/search/entry/1/"+param+"*/?format=HTML&isMobile=true"
        req = urllib.urlopen(url)
        data = req.read()
        bs = BeautifulSoup(data, 'html.parser')
        lst = bs.findAll("a", "ft")
        lst2=[]

        for s in range(0, len(lst)):
                lst2.append(lst[s].getText()[0]+lst[s].getText()[1])

        pri(lst2)
        
        lst2=[]




