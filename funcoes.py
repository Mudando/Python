#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 12:29:35 2021

@author: gilson
"""
"""
em python funções são definidas pela palavra reservada def

"""

# soma passando parametros


def somap(a, b):
    print(a+b)


somap(2, 3)

# sem passar parametros


def valores():
    a = int(input("Informe um valor para A: "))
    b = int(input("Informe um valor para B: "))
    return a, b


def soma():
    a = int(input("Informe um valor para A: "))
    b = int(input("Informe um valor para B: "))

    print(a+b)


soma()

# usando return


def soma(x, y):
    return x+y


def multiplica(x, y):
    return x*y


s = soma(3, 4)
m = multiplica(3, 4)

# agora vamos usar a função recursivamente, com os resultaods atribuidos anteiiroemente
print(s)
print(soma(s, m))
s = soma(3, 4)
m = multiplica(3, 4)

# agora vamos usar a função recursivamente, com os resultaods atribuidos anteiiroemente
print(s)
print(soma(s, m))
