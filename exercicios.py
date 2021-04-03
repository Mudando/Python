#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 09:55:26 2021

@author: gilson
"""
from math import sqrt

"""Verifica idade"""
idade = int(input("Informe sua idade: "))

if idade > 17:
    print ("Maior de idade.")
elif idade < 0:
        print("Idade Invalida")
else:
        print("Menor de idade")
        
        
"""Média de 2 numeros"""
A = float(input("Informe 1 valor para A: \n"))
B = float(input("Informe 1 valor para B: \n"))
media = (A+B)/2
print(media)

"""Eguação de 2 grau"""
A = float(input("Informe 1 valor para A: \n"))
B = float(input("Informe 1 valor para B: \n"))
C = float(input("Informe 1 valor para C: \n"))
delta = B**2 - 4*A*C
raiz = sqrt(delta) 

x1 = (-B +raiz)/(2*A)
x2 = (-B -raiz)/(2*A)

print("X1 : %f", x1)
print("X2 : %f", x2)


"""Ordenação com Selection Short"""
lista = [2,4,6,9,10,23,1,4,5,8]
for i in range(len(lista)):
    menor = i
    for j in range (i+1, len (lista)):
        if lista[j] < lista[menor]:
            menor = j
        if lista[i] != lista[menor]:
            aux = lista[i]
            lista[i] = lista[menor]
            lista[menor] = aux
print(lista)
