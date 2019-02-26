#! /usr/bin/env python
# -*- coding: utf8 -*-
# esto es un comentario en linea
"""
Esto es un comentario en bloque
"""
def mifuncion(fija,*dinamica):
    print("Hola "+fija)
    for muestra in dinamica:
        print(muestra)
mifuncion("Mundo","asdasd","adssadasd","sdasdasdasdas")
variable = 12345
print("Hola Mundo "+str(variable))
if variable is 1234:#if variable == 1234
    print("Si")
else:
    print("No")