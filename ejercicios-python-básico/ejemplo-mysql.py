#!/usr/bin/env python
# -*- coding: utf8 -*-
"""
pip install pymysql
"""
import sys
import pymysql
try:
    conector = pymysql.connect(host='localhost',
    port=3306,
    user='curso',
    passwd='curso',
    db='curso')

    cur = conector.cursor()
    """
    cur.execute("select * from alumnos")
    filas = cur.fetchall()
    for rows in filas:
        print(rows)
    """
    cur.execute("select * from alumnos where dui = %s",('1-8'))
    filas = cur.fetchall()
    for rows in filas:
        print(rows)
    """
    sql_insert = "insert into alumnos (dui,nombre,apellido) values (%s,%s,%s)"
    cur.execute(sql_insert,("1-8","Ronald","McDonald's"))
    """
    conector.commit()
    conector.close()
except Exception as e:
    sys.exit(e)
