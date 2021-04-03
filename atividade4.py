#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 19:44:49 2021

@author: gilson
"""


from functools import reduce

lista = [1,2,3,4,5,6,7,8,9,10]
lista2 = reduce(lambda x,y: x+y, lista)
print(lista2)
