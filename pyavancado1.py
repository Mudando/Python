#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 20:43:17 2021

@author: gilson
"""
#A lista y vai recebero quadrado da lista x
print("agora usando FOR normal")
x = [1, 2, 3, 4, 5]
y = []
for i in x:
    y.append(i**2)

print (x)
print (y)


#A lista B vai recebero quadrado da lista A
print("agora usando comprehension")
a = [3, 2, 3, 2, 6]
b = [i**2 for i in a]
print(a)
print(b)



#A lista C vai recebero os números impares de A
print("agora usando comprehension")
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = [i**2 for i in a]
c = [ i for i in a if i%2==1]
print(a)
print(b)
print(c)
