#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 11:41:37 2021

@author: gilson
"""

#paramnetros para manipulação de Arquivos
#r = somente leitura
#w = escrita(caso o arquivo já exista, ele será apagado e um novo será feito)
#a = leitura e escrita(Adiciona o novo conteúdo no fim do arquivo)
#r+ = leitura e escrita
#w+ = escrita(o modo w+, assim como o w, também apaga o conteúdo anterior do arquivo)
#a+ = leitura e escrita (abre os arquivos para atualização)

"""
read()  lê 1 arquivo inteiro
readline()  lê uma linha
readlines()  lê 1 arquivo e armazena em uma lista

lembrando que toda vez que abrimos 1 arquivo é importante
fechar depois com a função close(), pois se não pode dar erro
tipo não gravar

"""

#variável que vai receber o arquivo

arquivo = open("arquivos.txt")
#Imprimindo agora ele vai mostrar somente as informações do arquivo nãoo que tem dentro
print (arquivo)

#Agora usando as funções
#redlines, vai ler todas as linhas do arquivo e jogar dentro de uma lista
linhas = arquivo.readlines()
print (linhas)

#usando for Agora
for linha in linhas:
    print(linha)
    
arquivo.close()

arquivo2 = open("arquivos.txt")    
#Fazendo a leitura de tudo usando read e jogando tudo dentro de 1 unica variável
texto_completo = arquivo2.read()
print (texto_completo)
arquivo2.close()

#Criando 1 arquivo, iremos utilizar o metodo w
w = open("arquivo3.txt", "w")
#gravando coisas no arquivo criado
w.write("Este é o novo arquivo")
#lembrando que toda vez que abrimos 1 arquivo é importante fechar depois
w.close()


#Criando 1 arquivo, iremos utilizar o metodo a, se der certo a cada vez que 
#executarmos vai gravar novamente
w = open("arquivo4.txt", "a")
#gravando coisas no arquivo criado
w.write("Este é o novo arquivo\n")
#lembrando que toda vez que abrimos 1 arquivo é importante fechar depois
w.close()
