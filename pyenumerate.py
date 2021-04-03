#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 18:37:56 2021

@author: gilson
"""

lista = ["Abacate", "Banana", "Uva"]
#para obter os nomes dos itens e o indice a forma mais facil é suar um for
for i in range(len(lista)):
    print (i, lista[i])

print(".........................")

#utilizando enumerate agora
for i, nome in enumerate(lista):
    print (i, nome)
