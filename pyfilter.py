#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 19:06:57 2021

@author: gilson
"""

#O filter, vai pegar uma determinada lista e vai filtrar uma determinada condição
#para adicionar em outra lista

def pares (i):
    if i %2 == 0:
        return i


def impares (i):
    if i %2 == 1:
        return i


lista = [1, 2, 3, 4, 5, 6, 7, 8, 12, 23, 1,2, 12, 14, 15, 16, 23,4, 76, 45, 89]

listapares = filter(pares, lista)
listaimpar = filter(impares, lista)
print(list(listapares))

print(list(listaimpar))
