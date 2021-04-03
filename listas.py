lista = ["Abacaxi", "Melancia", "Morango", "Uva"]
lista2 = [1, 2, 3, 4, 5]
lista3 = ["abacate", 35, 4.6, True]

"""adiciona novas coisas na lista"""
lista.append("Mamão") 

"""Verifica se algo está na lista"""
if 7 in lista2:
    print("7 está na lista")
else:
    print("7 não está na lista")
print(lista)

"""Remover elementos de uma lista, usando paramentos para definir o 
intervalo no caso vai exluir do item 2 até o final"""
del lista[2:]
print (lista)
#Exluir todo mundo
del lista[:]
print (lista)

#Criar lista em branco e ir preenchendo aos poucos
lista4 = []
lista4.append("Teste")
lista4.append(2)
print (lista4)

#Ordenar lista, lembrando que ele altera a lista que já existe
lista5 = [1, 3, 6, 4, 89, 34, 15, 11, 35, 60]
lista5.sort()
print (lista5)

#Ordenar lista de forma decrescente, lembrando que ele altera a lista que já existe
lista7 = [1, 3, 6, 4, 89, 34, 15, 11, 35, 60]
lista7.sort(reverse=True)
print (lista7)
print (lista8)

lista10 = ["Bola", "Abacante", "Livro"]
lista10.sort()
print (lista10)

#Ordena uma função, mas requer que retorne um valor, retorna a lista ordenada sem alterar
lista6 = [3, 6, 4, 1, 8, 19, 21, 54, 61, 9, 24, 32]
lista6 = sorted(lista6)
print (lista6)

lista11 = ["Bola", "Abacante", "Livro"]
lista11 = sorted(lista11)
print (lista11)

#Reverte uma lista
lista8 = [3, 6, 4, 1, 8, 19, 21, 54, 61, 9, 24, 32]
lista8.reverse()
print (lista8)
lista9 = ["Bola", "Abacante", "Livro", True, False, 1, 2]
lista9.reverse()
print (lista9)


