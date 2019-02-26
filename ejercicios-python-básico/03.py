#! /usr/bin/env python
# -*- coding: utf8 -*-
# Sintaxis del lenguaje llamadas recursivas
#import sys
def jugar(intento=1):
    respuesta = input("¿De qué color es una naranja? ")
    if respuesta != "naranja":
        if intento < 3:
            print("\nYOU FAIL xD Inténtalo de nuevo")
            intento += 1
            jugar(intento) # Llamada recursiva
        else:
            print("\nPerdiste!")
    else:
        print("\nGanaste!")
jugar()
