#! /usr/bin/env python
# -*- coding: utf8 -*-
import sys
import requests
import bs4 as bs
# declarar la url
url = "https://www.siman.com/elsalvador/televisores/full-hd.html"
#url = ['sitioweb1.com','sw2.com']
r = requests.get(url)
soup = bs.BeautifulSoup(r.content, 'html.parser')
divs = soup.find_all("li", class_="col-xs-4")
filename = "siman-tv.csv"
f = open(filename, "a")
for d in divs:
        url_producto = d.a["href"]
        producto = d.a["title"]
        imagen = d.a.img["src"]
        lsoup = bs.BeautifulSoup(r.content, 'html.parser')
        contenedor = lsoup.find_all("div", class_="product-description")
        for prcs in contenedor:
                sku = getattr(prcs.find('p', attrs={'class': 'upc'}), "text")
                xsoup = bs.BeautifulSoup(r.content, 'html.parser')
                cajaprecio = xsoup.find_all("div", class_="price-box")
                #print cajaprecio
                for ps in cajaprecio:
                        precio = getattr(ps.find('span', attrs={'class': 'price'}), "text")
                        #print precio
                        #break
	        f.write(u' '.join((imagen +";"+ url_producto +";"+ producto + ";" + precio + "\n")).encode('utf-8'))
f.close()