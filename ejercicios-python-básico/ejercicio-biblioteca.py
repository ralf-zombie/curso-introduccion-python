#!/usr/bin/env python
# -*- coding: utf8 -*-
import os
import sys
import pymysql
try:
    conector = pymysql.connect(host='localhost',
    port=3306,
    user='curso',
    passwd='curso',
    db='curso',
    charset='utf8'
    )

    def agregar(conec):
        print("Ingresar un nuevo libro:\n")
        isbn = input("Agregar ISBN: ")
        titulo = input("Agregar Título: ")
        anio = input("Agregar Año: ")
        autor = input("Agregar Autor: ")            
        """
        isbn = raw_input("Agregar ISBN: ")
        titulo = raw_input("Agregar Título: ")
        anio = raw_input("Agregar Año: ")
        autor = raw_input("Agregar Autor: ")
        """
        cur = conec.cursor()
        sql_insert = "insert into biblioteca (isbn,titulo,anio,autor) values (%s,%s,%s,%s)"
        cur.execute(sql_insert,(isbn,titulo,anio,autor))
        conector.commit()
        conector.close()
        menu()
    def editar(conec):
        cur = conec.cursor()
        print("Editar un libro:\n")
        """
        id = raw_input("Ingrese el ID del libro: ")
        isbn = raw_input("Agregar ISBN: ")
        titulo = raw_input("Agregar Título: ")
        anio = raw_input("Agregar Año: ")
        autor = raw_input("Agregar Autor: ")
        """
        id = input("Ingrese el ID del libro: ")
        isbn = input("Agregar ISBN: ")
        titulo = input("Agregar Título: ")
        anio = input("Agregar Año: ")
        autor = input("Agregar Autor: ")        
        #Reviso si existe o no el id a editar
        coincidencia = "select id from biblioteca where id = %s"
        existe = cur.execute(coincidencia,(id))
        if not existe:
            print("No existe ID para editar. Intente nuevamente")
        else:
            sql = "update biblioteca set isbn=%s,titulo=%s,anio=%s,autor=%s where id = %s"
            cur.execute(sql,(isbn,titulo,anio,autor,id))
            conector.commit()
            conector.close()
            menu()
    def buscar(conec):
        print("Buscar un libro:\n")
        #isbn = raw_input("Ingrese ISBN a buscar: ")
        isbn = input("Ingrese ISBN a buscar: ")
        sql = "select * from biblioteca where isbn = %s"
        cur = conec.cursor()
        cur.execute(sql,(isbn))
        filas = cur.fetchall()
        for rows in filas:
            print(rows)
        conector.close()
        #menu()
    def borrar(conec):
        cur = conec.cursor()
        print("Borrar un libro:\n")
        #id = raw_input("Ingrese el ID del libro: ")
        id = input("Ingrese el ID del libro: ")
        coincidencia = "select id from biblioteca where id = %s"
        existe = cur.execute(coincidencia,(id))
        if not existe:
            print("No existe ID, no se puede eliminar")
        else:
            sql = "delete from biblioteca where id = %s"
            cur.execute(sql,(id))
            conector.commit()
            conector.close()
        menu()
    def menu():
        print("""
        Bienvenido a la Biblioteca del Curso\t
        Escoja las opciones:\t
        """)
        #opciones = raw_input("""
        opciones = input("""
        (1) Agregar nuevo libro\t
        (2) Editar libro por ID\t
        (3) Borrar libro por ID\t
        (4) Buscar libro por ISBN o TÍTULO
        (5) Salir del programa
        """)
        opciones = int(opciones)
        if opciones == 1:
            agregar(conector)
        elif opciones == 2:
            editar(conector)
        elif opciones == 3:
            borrar(conector)
        elif opciones == 4:
            buscar(conector)
        elif opciones == 5:
            os.system("clear")
        else:
            menu()
    menu()

except Exception as e:
    sys.exit(e)
