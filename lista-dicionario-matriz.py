# 1 - Crie uma estrutura de repetição para fazer a leitura de 5 números inteiros e os armazene dentro de uma lista. Após a leitura, crie outra estrutura de repetição para somar todos os valores digitados

lista =[]
for _in range (1,6):
       valor = int(input('Digite o valor: '))
       lista.append(valor)

soma = 0
for i in range(len(lista)):
       soma+= lista[i]
print('Soma: ' ,soma)
#-------------------------------

import numpy as np
np.array(lista).sum()

#-------------------------------

# 2 - Crie um dicionario para armazenar o nome e a nota de 3 alunis, fazeno a leitura dos valores por meio de uma estrutura de repetição. Depois crie uma nova estrutura de repetição para somar as notas e retornar a média

alunos = {}
  for _in range(1,4):
    nome = input('Digite o nome: ')
    nota = float(input('Digite a nota: '))
    alunos[nome]=nota
    
soma = 0 
for nota in alunos.values():
  soma+=nota
print('Média: ', soma/3)

# 3 - Data a matriz abaixo, construa uma estrutura de repetição para percorrer e somar todos os elementos da matriz

matriz = np.array([3,4,1],[3,1,5])

#matriz.shape 
#para visualizar o formato

soma= 0 
for i in range(matriz.shape[0]):
  for j in range(matriz.shape[1]):
    soma += matriz[i][j]
print('Soma :' , soma)
