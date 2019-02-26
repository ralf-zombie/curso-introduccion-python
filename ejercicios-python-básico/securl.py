#!/usr/bin/env python
# -*- coding: utf8 -*-
import re
import hashlib
import codecs

def hasher(*parts):
    h = hashlib.sha512()
    for part in parts:
        h.update(part)
    return h.digest()

def baseN(num, base=10):
    digitos = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = []
    while num > 0:
        digito = num % base
        result.append(digitos[digito])
        num //= base
    return "".join(result[::-1])
def main():
    secreto_servidor = "935826fj0h75t928j0927ed59h1573fj09456Akoir41f"
    URLSEC = re.compile(".*/pdf/([^/]*)/([^/]*)(?:/([^/]*))?")
    #URL EJEMPLO
    url = "https://netstream.cl/pdf/ALGO/K28000000FECDA3DOC/ibHnbZdxmzoftb1WsYdEWRDkj"
    institucion, folio, codigo_recibido = URLSEC.match(url).groups()
    print(repr((institucion, folio, codigo_recibido)))
    hash = int(hasher(institucion, folio, secreto_servidor).encode('hex'), 32)
    hash %= (62 ** 25)
    codigo_esperado = baseN(hash, 62).rjust(6, "0")
    if codigo_recibido is None:
        print(url + "/" + codigo_esperado)
    else:
        print(codigo_recibido, codigo_esperado, codigo_recibido == codigo_esperado)
main()