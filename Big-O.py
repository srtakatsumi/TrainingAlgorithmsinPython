#Big-O = O é a complexidade de um algoritmo que foi desenvolvido
# Função 1 - O(n)
# essa função ela tem 11 passos
def soma1(n):
  soma= 0
  for i in range(n+1):
    soma += i
  return soma
# ex: %timeit soma(10)

# Função 2 
# essa função ela tem 3 passos
# O(3)
def soma2(n):
  return (n * (n+1)) / 2

# ex: %timeit soma2(10)

# Função 3
def lista1():
  lista = []
  for i in range(1000):
    lista +=[i]
  return lista
# ex: %timeit soma2(10)

# Função 4
def lista2():
  return range(1000)
# para visualizar em lista os números
#for i in l: 
#  print(i)


# Funções Big-O 

from math import log
import numpy as no
import matplotlib.pyplot as plt

n = np.linspace(1,10,100)

labels = ['Constant', 'Logarithmic', 'Linear', 'Log Linear' , 'Quadratic','Cubic','Exponential']
big_o = [np.ones(n.shape), np.log(n),n, n*np.log(n), n**2,n**3,2**n]

plt.figure(figsize=(10,8))
plt.ylim(0,100)
for i in range(len(big_o)):
  plt.plot(n,big_o[i],label = labels[i])
plt.legend()
plt.ylabel('Runtime')
plt.xlabel('n')



# Constant - O(1)

[40] lista = [1,2,3,4,5]

def constant(n):
  print(n[0])
  
# Linear - O(n)
def linear(n):
  for i in n:
    print(i)
    

# Quadratic - O(n^2) - polynomial
# O(1) +  O(5) + O(n) + O(n) + O(3) 
# O(9) + O2(n) ->  O(n) 
def quadratic(n):
  for i in n:
    for j in n:
      print(i, j)

# Combination
def conbination(n):
  # O(1)
  print(n[0])
  
  # O(5)
  for i in range(5):
    print('test', i)
  # O(n)
  for i in n:
    print(i)
  # O(n)
  for i in n:
    print(i)
  # O(3)
  print('Python')
  print('Python')
  print('Python')

