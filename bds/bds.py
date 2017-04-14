#!/usr/bin/python
#coding:utf-8

import requests
from bs4 import BeautifulSoup
import os
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
s = requests.Session()
r = s.get('http://123.57.87.17/index', headers = headers)
soup = BeautifulSoup(r.text, 'lxml')
divs = soup.find_all("figure", class_='product')
for div in divs:
    #print(div.find_all('img'))
    imglist = div.img.get('src') or div.img.get('data-src')
    url = 'http://123.57.87.17/'+imglist


    os.system('wget %s' % url)

