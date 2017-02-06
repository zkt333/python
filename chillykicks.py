import re
from bs4 import BeautifulSoup
import requests
import webbrowser
import time
import winsound
def chilly():
 j = 0
 while j < 1:
    url = 'http://chillykicks.com/collections/size-13'
    source = requests.get(url)
    text = source.text
    soup = BeautifulSoup(text)
    showname = []
    shoelink = []
    for key in soup.findAll('a',{'class':'product-image'}):
        href  = key.get('href')
        shoelink.append(href)
        for name in key.findAll('img'):
            newname = name.get('alt')
            showname.append(newname)
    shoelink.remove(shoelink[0])
    for k in showname:
        if 'Yeezy' in k.split(' ') or '350' in k.split(' ') or 'yeezy' in k.split(' '):
            j = 1
            number = showname.index(k)
            url = shoelink[number]
            newurl = 'http://chillykicks.com'+ url
            souce = requests.get(newurl)
            text = souce.text
            findid = re.compile(r'\"id\"\:\d{11}')
            lid = findid.findall(text)
            i = 5
            id = ''
            while i < len(lid[0]):
                id += lid[0][i]
                i += 1
            addurl = 'http://chillykicks.com/cart/'+ id +':1'
            webbrowser.open(addurl)

    time.sleep(1)
    print('not found')







chilly()

