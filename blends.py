import re
from bs4 import BeautifulSoup
import requests
import webbrowser
import winsound
import time
def scanblends():
    loop = 0
    while loop < 1:
      url = 'https://www.blendsus.com/collections/new-arrivals'
      soucecode = requests.get(url)
      text = soucecode.text
      soup = BeautifulSoup(text)





      for h in soup.findAll('a'):
              href = h.get('href')
              link = 'https://www.blendsus.com' + href
              for key in link.split('-'):
                  #链接关键词
                  if '93/17' in key:

                      newurl = link
                      print(newurl)
                      soucecode = requests.get(newurl)
                      text = soucecode.text
                      findsize = re.compile(r'\"title\"\:\"\d*\.?\d?\"')
                      findsku = re.compile(r'\"id\"\:\d{11}\,\"')
                      findinventory = re.compile(r'\"inventory_quantity\"\:\d+')
                      inventory = findinventory.findall(text)
                      size = findsize.findall(text)
                      #print(size)
                      sku = findsku.findall(text)

                      #stop loop
                      loop = 2


                      # input the size you want, I get 9.5 for example
                      number = size.index('"title":"9.5"')

                      resku = sku[number]
                      combine = zip(size, inventory)
                      for x, y in combine:
                          print(x, y)

                      i = 5
                      w = ''
                      while i < 16:
                          w += resku[i]
                          i += 1
                      print(w)
                      addurl = "https://www.blendsus.com/cart/" + w + ':1'
                      webbrowser.open_new(addurl)
                      winsound.Beep(2500, 1000)
                      winsound.Beep(2500, 1000)
      print('not found')
      time.sleep(1)
scanblends()