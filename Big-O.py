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

