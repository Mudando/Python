#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 19:54:58 2021

@author: gilson
"""

import pygame

# iniciar os módulos
pygame.init()

# criando janela ou qualquer outro nome que queira, primeiro iremos credenciar as variáveis
janela = pygame.display.set_mode((500, 500))

# iremos criar agoa o título da janela
pygame.display.set_caption("Titulo janela")

# iremos para o loop agora, para simplificar é uma variavel que irá receber um valor verdadeiro bool
loop = True
while loop:
    # idemor colocar os eventos agora, tipo o comando abairo irá pegar todos os eventos do pygame
    # e irá chamar pelo nome que definimos abairo no caso event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
