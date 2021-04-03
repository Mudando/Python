#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 19:30:37 2021

@author: gilson
"""
from functools import reduce

#função reduce
#recebe uma lista e retorna 1 unico valor dessa lista
#Dá de usar para receber a soma dos valores dos elementos de uma lista

def soma(x, y):
    return x+y


lista = [1, 2, 3, 4, 12, 34, 5, 6, 7, 23]

soma = reduce(soma, lista)
print(soma)
