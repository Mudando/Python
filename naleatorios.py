#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 14:42:57 2021

@author: gilson
"""

import random

#numero aleatório de 0 a 10
numero = random.randint(0,10)
print (numero)

#Forcar o python a selecionar sempre o mem numero
random.seed(1)
numero2 = random.randint(0,10)
print (numero2)

#Seleciona o numero aleatório de uma lista
lista = [1,2,4,6,3,7,8,9,10]
numero3 = random.choice(lista)
print (numero3)

