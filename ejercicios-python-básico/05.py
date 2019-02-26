#! /usr/bin/env python
# -*- coding: utf8 -*-
# web scraping
"""
@author ralf
pip install requests
pip install bs4
"""
import sys
import requests
import bs4 as bs#alias
try:
    # Array de direcciones web de donde obtenemos la metadata
    url_txt = ['https://www.baradent.cl/categorias/fresas-y-pulidores',
    'https://www.baradent.cl/categorias/fresas-y-pulidores?p=2',
    'https://www.baradent.cl/categorias/fresas-y-pulidores?p=3']
    filename = "ejemplo.csv"
    f = open(filename, "wb")#Se abre el archivo en forma binaria en Python 3
    for ss in url_txt:
        #r = requests.get(ss,auth=('user','pass'))
        r = requests.get(ss)
        soup = bs.BeautifulSoup(r.content, 'html.parser')
        #Por cada sitio web se debe manejar el dom de etiquetas
        divs = soup.find_all("li", class_="item")
        for item in divs:
            imagen = item.div.a.img["src"]
            nombre = item.h2.a.text
            urlorigen = item.h2.a["href"]
            url_producto = [item.h2.a["href"]]
            for link in url_producto:
                rq = requests.get(link)
                lsoup = bs.BeautifulSoup(rq.content, 'html.parser')
                detallesku = lsoup.find_all("div", class_="sku")
                descripcion = lsoup.find_all("div", class_="panel")
                for psku in detallesku:
                    sku = getattr(psku.find('span', attrs={'class': 'value'}), "text")
                    break
                for pdetalle in descripcion:
                    desc = pdetalle.div.text
                    format_desc = desc.replace(",", " ").strip()
                    break
            format_nombre = nombre.replace(",", " ").strip()
            precio = getattr(item.contents[9].find('span', attrs={'class': 'price'}), "text", 0).strip()
            precio_format = precio.replace(".","").lstrip("$")
            f.write(u' '.join((format_nombre + ";", precio_format + ";", imagen +";", format_desc + "Baradent" + ";", sku + ";", urlorigen + ";" , "Baradent;", "Fresas y Pulidores" + "\n")).encode('utf-8'))
    f.close()
except Exception as e:
    sys.exit(e)
