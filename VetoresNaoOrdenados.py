#

class VetorNaoOrdenado: 
  def _init_(self, capacidade):
    self.capacidade = capacidade
    self.ultima_posicao = -1
    self.valores = np.empty(self.capacidade, dtype=int)
  # O(n)  
  def imprime(self):
    if self.ultima_posicao ==-1
      print('O vetor está vazio')
    else: 
      for i in range(self.ultima_posicao + 1):
        print(i, ' - ' , self.valores[i])
# O(1) -  O(2)
  def insere(self, valor):
    if self.ultima_posicao == self.capacidade -1
      print('Capacidade máxima atingida)
    else:  
      self.ultima_posicao +=1   
      self.valores[self.ultima_posicao] = valor
  # O(n)          
  def pesquisar(self, valor): 
     for i in range(self.ultima_posicao +1 ):
       if valor == self.valores[i]:
         return i
     return -1
            
  # O(n)             
  def excluir(self, valor): 
     posicao = self.pesquisa(valor)
     if posicao == -1:
         return -1
     else:
         for i in range(posicao, self.ultima_posicao):
          self.valores[i+1]
         self.ultima_posicao -= 1
# como testar
# vetor = VetorNaoOrdenado(5)

            
