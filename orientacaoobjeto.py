# Orientação a Objeto - classe e objeto

# Agrupamento de objetos similares que apresentam os mesmos atributos e métodos

#Molde de bonecos de gesso
 # Define o formato e tamanho
 # O molde é sempre o mesmo, porém, os objetos gerados podem ter características variadas, respeitando a estrutura básica do molde
# É possivel utilizar o mesmo molde e só trocar a cor, então se torna a base para a criação
# Visto podemos aplicar essa tecnica no código, desenvolvendo um código e depois chamando o novamente para "criarmos uma nova cor" do código

# Podemos ter caracteristicas = atributos
#ex: cor, tamanho, nº de patas e raça

# ações (seria os metods)
#ex: latir, correr, morder, brincar

# trocando o exemplo para uma calculadora 
#Atributos = Cor, marca, tamanho, data de fabricação > Tipo: string, listas, tuplas
#Metodo = somar, subtrair, dividir, multiplicar > Funções

class Triangulo: 
  def _init_(self,lado1,lado2,lado3,base,altura):
    self.lado1 = lado1
    self.lado2 = lado2
    self.lado3 = lado3
    self.base = base
    self.altura = altura
 def area(self):
  return(self.base * self.altura) / 2
  
def tipo(self):
  if self.lado1 > self.lado2 + self.lado3:
    return 'não é um triângulo'
  elif self.lado1 == self.lado2 or self.lado1 == self.lado3 or self.lado1 == self.lado2:
    return 'triângulo isóceles'
  else: 
    return 'outro tipo de triângulo'


  
