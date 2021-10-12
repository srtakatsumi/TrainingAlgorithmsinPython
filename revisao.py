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
                           
                           
                           
                           
                           
                           
                           
 
