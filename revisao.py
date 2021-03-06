# 1
# Ler uma temperatura em graus Celsius e apresentá-la convertida em graus Fahrenheit. 
#A fórmula de conversão é F = (9 * C + 160) / 5, na qual F é a temperatura em Fahrenheit e C é a temperatura em graus Celsius

# - Função para ler e retorna o valor da temperatura (não recebe parâmetro)
def ler_temperatura():
  temperatura = float(input('Digite a temperatura em graus Celsius: '))
  return temperatura
# - Função para fazer o cálculo (recebe como parâmetro a temperatura em graus Celsius)
def converter(temperatura_celsius):
  temperatura_f = (9 * temperatura_celsius + 160) / 5
  return temperatura_f
# - Função para mostrar o resultado, recebendo como parâmetro o valor e fazendo a impressão
temperatura_c = ler_temperatura()
temperatura_f = converter(temperatura_c)
mostrar(temperatura_f)


#  2
# Efetuar o cálculo da quantidade de litros de combustível gasto em uma viagem, utilizando um automóvel que faz 12 Km por litro. 
#Para obter o cálculo, o usuário deve fornecer o tempo gasto na viagem e a velocidade média durante ela. 
#Desta forma, será possível obter a distância percorrida com a fórmula DISTANCIA = TEMPO * VELOCIDADE. 
#Tendo o valor da distância, basta calcular a quantidade de litros de combustível utilizada na viagem, com a fórmula: LITROS_USADOS = DISTANCIA / 12. O programa deve apresentar os valores da velocidade média, tempo gasto na viagem, a distância percorrida e a quantidade de litros utilizada na viagem

# - Função para ler os valores (não recebe parâmetro e retorna os dois valores)
def leitura():
  tempo = float(input('Digite o tempo de viagem: '))
  velocidade = float(input('Digite a velocidade media: ))
  return tempo, velocidade
                           
# - Função para calcular a distância (recebe como parâmetro o tempo e a velocidade e retorna a distância)
def calcula_distancia(tempo,velocidade):
   return tempo + velocidade
                           
# - Função para calcular a quantidade de litros (recebe como parâmetro a distância e retorna os litros)
def calcula_litros(distancia):
   return distancia /12        
                           
# - Função para apresentar o resultado (recebe como parâmetro os valores e somente imprime o resultado)
def imprime(velocidade, tempo, distancia, litros):
   print('Velocidade: ', velocidade)
   print('Tempo: ', tempo)                           
   print('Distancia: ', distancia)                           
   print('Litros: ', litros)                     
                           
                           
#3
# Crie um arquivo .py com duas funções
# - Função para ler um string (recebe como parâmetro uma mensagem e retorna o que o usuário digitou)
# - Função para ler um número float (recebe como parâmetro uma mensagem e retorna o que o usuário digitou)

#em um arquivo defina
def ler_string(mensagem):
   return input(mensagem) 
def ler_float(mensagem):
   return float(input(mensagem))

# em outro arquivo                           
import leitura as lt
text = lt.ler_string():
print(text)
number = lt.flaot():
print(number)                           
                        

# 4                           
# Crie uma lista vazia e faça a leitura de dois valores do tipo float, colocando cada um dos valores nas primeiras posições da lista (o valor1 ficará na posição 0 da lista e o valor2 ficará na posição 1 da lista). Faça a divisão dos dois valores e trate as seguintes exceções:
# - ValueError: se o usuário digitar um caracter
# - ZeroDivisionError: se o usuário digitar zero e ocorrer erro na divisão
# - IndexError: caso a divisão seja feita levando em consideração posições que não existem na lista
# - KeyboardInterrupt: caso o usuário interrompa a execução
# Mostre uma mensagem personalizada na ocorrência de cada um desses erros


lista = []
try: 
 lista.appendi(float(input('Digite o primeiro valor: ')))
 lista.appendi(float(input('Digite o segundo valor: ')))
 division = lista[0] / lista[1]
except ValueError:
  print('Erro! Valor inválido')
except ZeroDivisonError:
  print('Erro! Divisão por zero')
except IndexError:
  print('Erro! Índice inválido')
except KeyboardInterrupt:
  print('Usuário interrompeu a execução')  
else:
  print(f'A divisão acima é {division}')
  break
                           
                           
# 5   
# Considerando o dicionário com o nome dos alunos e suas respectivas notas abaixo, crie uma estrutura de repetição para percorrer cada elemento do dicionário para gravar cada aluno em um novo arquivo de texto
# - Cada aluno deve ocupar uma linha do novo arquivo de texto
# - O formato deve ser: nome,nota (Pedro,8.0)
# - Após a criação do arquivo de texto, faça a leitura do arquivo e mostre todos os alunos
# alunos = {'Pedro': 8.0, 'Maria': 10.0, 'Amilton': 7.5}
alunos = {'Pedro': 8.0, 'Maria': 10.0, 'Amilton': 7.5}

with open('alunos.txt', 'w') as arquivo:
  for aluno, nota in alunos.items():
    arquivo.write(f'{aluno}, {nota}\n')
    
with open('alunos.txt', 'r') as arquivo:
  for linha in arquivo:
    print(linha)                           
# 6                           
#Crie expressões regulares para extrair as seguintes informações do texto abaixo (use a função findall):
text = "Minha casa fica na Rua Fulano Torres, 1999 o CEP é 00800-666 e meu site é https://www.srtakatsumi.com"
import re
#- Números
re.findall('\d', text)
#- CEPs
re.findall('d{5}-\d{3}',text)
#- URLs
re.findall('https?://[A-Za-z0-9./]+', text)


#Crie uma classe chamada aluno com os seguintes atributos:
#- Nome
#- Nota 1
#- Nota 2
#- Crie um construtor para a classe (__init__)
class Aluno: 
  def _init_(self,nome,nota1,nota2,nota3,media):
    self.nome = nome
    self.nota1 = nota1
    self.nota2 = nota2
    self.media - 0.0

#Crie as seguintes funções (métodos):
#- Calcula média, retornando a média aritmética entre as notas

 def media(self):
  self.media = (self.nota1 + self.nota2 ) /2
  return self.media
                           
#- Mostra dados, que somente imprime o valor de todos os atributos
def mostra_dados(self):
   print('Nome : ', self.nome)                         
   print('Nota 1 : ', self.nota1)                         
   print('Nota 2 : ', self.nota2)                                                    
   print('Média : ', self.media) 
                           
#- Resultado, que verifica se o aluno está aprovado ou reprovado (se a média for maior ou igual a 6.0, o aluno está aprovado)
def resultado(self):                           
  if self.media => 6.0 :
    print('Aprovado')
  else: 
    print ('Reprovado')
                           
#Crie dois objetos (aluno1 e aluno2) e teste as funções
# Teste
# aluno1 = Aluno('João', 7.0, 2.0)
# aluno1.resultado()
# retorna Reprovado                           
                           

                           
                           
                           
                           
                           
                           
 
