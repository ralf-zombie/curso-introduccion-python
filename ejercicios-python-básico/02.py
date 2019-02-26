#! /usr/bin/env python
# -*- coding: utf8 -*-
# Sintaxis del lenguaje llamadas de retorno
def funcion():
    return "Hola Mundo"
def llamada_de_retorno(func=""):
    """Llamada de retorno a nivel global"""
    return globals()[func]()
retorno = llamada_de_retorno("funcion")
print(retorno)
# Llamada de retorno a nivel local
nombre_de_la_funcion = "funcion"
print(locals()[nombre_de_la_funcion]())
