#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 17:32:13 2021

@author: gilson
"""

#Testa seguencias iguais
seq1 = input("Digite a Seguencia 1: ")
seq2 = input("Digite a Seguencia 2: ")

if seq1 == seq2:
    print("Seguencias iguais.")

else:
    print("Seguencias diferentes")


#seguencias iguais utilizando o modulo re
import re

seq3 = input("Digite a Seguencia 1: ")
seq4 = input("Digite a Seguencia 2: ")
busca = re.match(seq3, seq4)
if busca:
    print("Seguencias Iguais.")
    print(busca.group())
else:
    printf("seguencias diferentes.")


