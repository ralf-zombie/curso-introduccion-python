#! /usr/bin/env python
# -*- coding: utf8 -*-
# web scraping
"""
pip install bs4
pip install requests
"""
import sys
import requests
import bs4 as bs#alias
try:
    url = "https://www.lacuracaonline.com/elsalvador/productos/electronica/computadoras/portatiles.html"
    r = requests.get(url)
    soup = bs.BeautifulSoup(r.content, 'html.parser')
    #print soup
    listas = soup.find_all("li", class_="product-item")
    detalle = soup.find_all("div",class_="product-item-details")
    for objetos in listas:
        nombre = objetos.find_all("a", class_="product-item-link")
        vinculo = objetos.find_all("a", class_="product-item-link")
        for realnombre in nombre:
            print(realnombre.text)
    for info in detalle:
        marca = info.find_all("strong", class_="product-item-category")
        for detallemarca in marca:
            print(detallemarca.text)
except Exception as e:
    sys.exit(e)
