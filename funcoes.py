# - Trechos de programa que recebem um determinado nome e podem ser chamados várias vezes durante a execução
# - Principais vantagens: reutilização do código, modularidade e facilidade de manuntenção do sistema

# ------------------------------------------

# Função sem parâmentro e sem retorno
def mensagem():
  print('Texto da função')

# Função com passagem de parâmetro
def mensagem(texto):
  print(texto)
# -------------------  
def soma(a,b):
  print(a + b)

# Função com passagem de parâmetros e retorno
def soma(a,b):
  return a+b
# -------------------
#g = aceleração gravitacional / m = massa / h = altura / e = energia

def calcula_energia_potencial_gravitacional(m,h,g = 10):
  e = g * m * h
  return e
