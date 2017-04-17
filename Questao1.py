"""
Questao 1:

"""
import random

numeros = [1, 2, 3, 4, 5]
alunos = {"2010": "Lucas", "2011": "Luan", "2012": "Pedro"}
mensagemProva4 = ("")
print("Seja bem vindo(a) ao Programa da Prova 4")
print("Lista é um conjunto que contem uma ordem de números, identificados por índices.")
print("Dicionário é um conjunto que implementa mapeamentos, esses mapeamentos são acompanhados de chaves e valores.")
print("Estou pronto para manipular listas e dicionários na prova!")

cont = 0
sorteados = []
for x in range(0, 20):
        numSorteados = random.randint(0, 100)
        sorteados.append(numSorteados)
        cont +=1
        print("O valor da linha", x, "é", sorteados[x])

mensagemProva4 = "Prova sobre manipulação de listas e dicionários"
qtdLetras = len(mensagemProva4)
print("A quantidade de letras na variável 'mensagemProva4' é igual a:", qtdLetras)

mensagemProva4 = "Prova sobre manipulação de listas e dicionários. Prova de número 4."
print(mensagemProva4)






