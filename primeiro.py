"""teste """
from random import randint
var1 = 1  # inteiro
var2 = 1.1  # flutuante
var3 = "teste"  # string

    print(var1)
print(var2)
print(var3)

x = 1
y = 2
soma = x + y
print(x == y and soma >= x)

for i in range(1, 2, 2):
    print(i)

x = 123
y = randit[0, 1000]
if x > y:
    print("X maior que Y")

else:
    print("Y maior que X")


if x > y:
    print("X maior que Y")

else:
    print("Y maior que X")

x = 3
y = 2

if y > x:
    if y > 0 and y > x:
        print("Y maior que X \n Y é positivo ")
    elif y < x:
        print("Y menor que X e negativo")
    else:
        print("Y menor que X")

i = 0
while i < 10:
    print(i)
    i += 1


numero = input("Informe um valor: ")
print(numero)

"""Concatenação"""
teste = "Gilson"
teste2 = "Ricardo"
concatenar = teste + " " + teste2 + " " + "@"
print(concatenar)

"""Atribui o valor do tamanho"""
tamanho = len(concatenar)
print(tamanho)
"""inprime na posição"""
print (teste[0])
print(teste[1])
print(teste[2])

"""imprime no intervalo"""
print(concatenar[0:5])

"""Deixa Minusculo, lembrando que não altera a variavel só mostra minuscula"""
print(concatenar.lower())

"""Deixa Maiuscula, lembrando que não altera a variavel só mostra maiuscula"""
print(concatenar.upper())
"""Trasforma em minuscula"""
concatenar = concatenar.lower()
print(concatenar)

"""Trasforma em maiuscula"""
concatenar = concatenar.upper()
print(concatenar)

"""Remove spaços e caracteres especiais do final da string"""
print(concatenar.strip())

"""converte seguencia em uma lista, tipo imprime sem o que estiver nas aspas"""
minhaString = "O rato roel a roupa do rei"
minhaString = minhaString.split(" ")
print(minhaString)

"""Busca de substring, imprimi -1 caso não ache """
nome = "rei"
nomeBusca = "O rato roel a roupa do rei de roma"
busca = nomeBusca.find(nome)
print(busca)

"""imrpimir a partir do local que der o tamanho da busca anterior"""
print(nomeBusca[busca:])

"""Subistituir partes da string"""
nome = nomeBusca.replace("o rei", "a rainha")
print(nome)


