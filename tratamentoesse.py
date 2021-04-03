#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 16:06:56 2021

@author: gilson
"""

a = 2
b = 0

#ele vai tentar fazer a operação, caso aja erro vai acionar a exeção
try:
    print(a/b)
except :
    print("Não é permitido a divisão por 0")
