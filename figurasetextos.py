#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 20:33:58 2021

@author: gilson
"""
import pygame

#definido as cores

PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERMELHO = (255, 0 , 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)

#DEFININDO PI
PI = 3.1416

#inicializando os módulos de pygame
pygame.init()

#Criando a janela  com título figuras e textos
janela = pygame.display.set_mode((500, 400))
pygame.display.set_caption("Figuras e Textos")

#preenchendo o fundo da janela de branco
janela.fill(BRANCO)

#Trabalhando com Textos
fonte = pygame.font.Font(None, 48)
texto = fonte.render("Olá munddo", True, BRANCO, AZUL)
janela.blit(texto, [30, 150])

#desenhando figuras
pygame.draw.line(janela, VERDE, (60, 260), (420, 260), 4)
pygame.draw.circle(janela, VERMELHO, (300, 50), 20, 0)
pygame.draw.rect(janela, PRETO, (20, 20, 60, 40), 0)

#ATUALIZANDO E MOSTRANDO NA TELA O QUE JÁ FOI FEITO
pygame.display.update()

#iremos agora fazer o programa ficar aberto tempo suficiente
deve_continuar = True
while deve_continuar:
    #loop para checar os eventos
    for event in pygame.event.get():
        #condicional para sair do loop
        if event.type == pygame.QUIT:
            deve_continuar = False
pygame.quit()
