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
                           
                           
