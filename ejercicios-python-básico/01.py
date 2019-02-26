#! /usr/bin/env python
# -*- coding: utf8 -*-
# Sintaxis del lenguaje declarando un método o función
def saludo():
    print ("Hola Mundo")
def nuevo_saludo():
    return "Hola Mundo, otra vez"
def metodo_params(a,b):
    nombre = a+ ", "+ b #Concatenación es con +
    return nombre
def metodo_params_fijos(p_fijo, *dinamico, **llavevalor):
    return p_fijo
    for argumento in dinamico:
        return argumento
    for clave in llavevalor:
        return "El valor de", clave, "es", llavevalor[clave]
def calculo(apagar, descuento):
    return apagar - (apagar * descuento / 100)
#saludo()
#frase = nuevo_saludo()
#frase = metodo_params('Rodrigo','Alfaro Pinto')
#frase = metodo_params_fijos("Fixed", "arbitrario 1", "arbitrario 2", "arbitrario 3", clave1="valor uno", clave2="valor dos")
#print (frase)
datos = {"descuento": 10, "apagar": 1500}
mostrar = calculo(**datos)
print (mostrar)
