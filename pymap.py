#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 19:03:21 2021

@author: gilson
"""
#A função map vai pegar uma função e aplicar a todos os elementos de uma lista
#Mostrado de uma forma simples

def dobro(x):
    return x*2

valor = 2
print(dobro(valor))

#Em uma lista agora, se eu faço a mesma coisa ele só vai fazer uma cópia da lista
#tipo concatenando e não obtendo o dobro dos valores da lista
valor2 = [1, 3, 2, 4, 5, 6, 23, 7]
#print(dobro(valor2))

#por isso iremos utilizar o map
#primeiro chamamos a função, depois a lista  a quem queremos usar
valordobrado = map(dobro, valor2)
for v in valordobrado:
    print(v)

#Mas supondo agora que queremos usar a função dobro somente uma vez
#Com isso não precisamos criar uma função para isso, podemos simplismente usar
#uma função lambda, que vai criar a função na linha que iremos estar utilizando
#O objetivo dela é basicamente economizar espaço pois só usamos 1 unica vez
valordobrado2 = map(lambda i: i*2 , valor2)
for v in valordobrado2:
    print(v)




