#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 18:17:11 2021

@author: gilson
"""
import random
print("***************************************")
print("Olá, Bem vindo ao jogo de Adivinhação!!!")
print("***************************************")

numero_secreto = random.randrange(1, 101)
total_de_tentativas = 0
pontos = 1000

print("Qual nível de dificuldade?")
print("( 1 ) Fácil ( 2 ) Médio ( 3 ) Difícil ")

nivel = int(input("Escolha seu nível: "))

if(nivel == 1):
    total_de_tentativas = 20
elif(nivel == 2):
    total_de_tentativas = 10
elif(nivel == 3):
    total_de_tentativas = 5

for rodada in range(1, total_de_tentativas + 1):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    chute_str = input("Digite o seu número entre 1 e 100: ")
    print("Você digitou: ", chute_str)
    chute = int(chute_str)

    if(chute < 1 or chute > 100):
        print("Você deve digitar um número entre 1 e 100")
        continue
    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if (acertou):
        print("Você acertou e fez {} pontos!!!".format(pontos))
        break
    else:
        if(maior):
            print("Você errou! O seu número foi maior que o número secreto.")
        elif(menor):
            print("Você errou! O seu número foi menor que o número secreto.")
        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos

print("Fim De Jogo")