#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 17:59:09 2021

@author: gilson
"""

menu = 0


def abrirArquivo():
    nome = input("Digite o nome do arquivo que deseja abri:")
    arquivo = open(nome)
    return arquivo


def lerArquivo(arquivo):
    linhas = arquivo.readlines()
    for linha in linhas:
        print(linhas.strip())


while menu != 3:
    menu = int(input("1: Abir um novo arquivo \n2: Ler aquivo aberto \n3: Sair "))
    if menu == 1:
        abrirArquivo()
    elif  menu == 2:
        lerArquivo()
    elif menu != 1 & menu != 2:
        if menu != 3:
                print("Opção invalida\n")
