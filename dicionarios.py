#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 21:08:39 2021

@author: gilson
"""
#Os dicionários usam chave para identificar
#A diferenca de lista é que declaramos eles com {} 
#e usamos [] para fazer busca
#Cada item no dicionário é separado por : onde a chave vem primeiro
#E o meu valor vem depois, para adicionar outro item é so colocar virgula

meu_dicionario = {"A": "Abacate", "B" : "Banana", "C" : "Cacau", "D" :"Damasco" }

#imprimir a 1 posição devemos usar a chave A
print(meu_dicionario["A"])

#imprimir dicionario inteiro
print(meu_dicionario)

#navegando pelo dicionario e imprimindo as chaves
for chave in meu_dicionario:
        print(chave)


#navegando pelo dicionario e imprimindo os valores
for chave in meu_dicionario:
        print(meu_dicionario[chave])
        
#navegando pelo dicionario e imprimindo as chaves e os valores
for chave in meu_dicionario:
        print(chave + " : " + meu_dicionario[chave])
        
#Usando funções do python agora
#a função items retorna todos os itens e os trasforma em uma tupla
for i in meu_dicionario.items():
    print(i)
    
#Values retorna só os valores
for i in meu_dicionario.values():
    print(i)
    
#Keys retorna só as chaves
for i in meu_dicionario.keys():
    print(i)