# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
from pprint import pprint

def maannews(url):
  res = requests.get(url)
  soup = BeautifulSoup(res.text, 'html.parser')
  links = soup.select('.list-6__item')
  datez = soup.select('.list-6__date')
  print('------------Maan-News----------------------------')
  maan = []
  for idx, item in enumerate(links):
    title = item.get('title', None)
    href = item.get('href', None)
    datee = datez[idx].getText()
    maan.append({'title': title, 'link': href, 'date': datee})
  return maan

def rayafm(url):
  res = requests.get(url)
  soup = BeautifulSoup(res.text, 'html.parser')
  links = soup.select('h3')
  raya = []
  print('------------RayaFM-News----------------------------')
  for idx, item in enumerate(links):
    title = item.a.get('title', None)
    href = item.a.get('href', None)
    raya.append({'title': title, 'link': href})
  return raya

ra = rayafm('https://www.raya.ps/news/palestine-today?page=1')
ma = maannews('https://www.maannews.net/news?page=1')
with open("newsScraped.txt", "w") as myfi:
  for i in ra:
    for item, val in i.items():
      myfi.write(f"{item} : {val}\n")
  myfi.write("\n\n--------Raya-News--------\n\n")
  for i in ma:
    for item, val in i.items():
      myfi.write(f"{item} : {val}\n")
  myfi.write("\n\n--------Maan-News--------\n\n")

pprint(ra)
pprint(ma)
#pprint(maannews('https://www.maannews.net/news?page=2'))
