#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 18:47:38 2021

@author: gilson
"""

#supondo que temos 2 listas
#A lista 1 tem valores numericos e a 2 tem textos
lista1 = [1, 2, 3, 4, 5]
lista2 = ["abacate", "banana", "cacau", "manga"]

#dai supondo que eu quero imprimir as 2 listas concatenando elas
#com isso usamos o Zip, que vai compactar as 2 listas em somente uma
#para que possamos percorer elas com um único for

for numero, nome in zip(lista1, lista2):
    print(numero, nome)

#com 3 listas agora
lista3 = [1, 2, 3, 4, 5]
lista4 = ["abacate", "banana", "cacau", "manga"]
lista5 = ["2 reais", "2,5 reais", "5 reais", "3 reais"]


for numero, nome, valor in zip(lista3, lista4, lista5):
    print(numero, nome, valor)




