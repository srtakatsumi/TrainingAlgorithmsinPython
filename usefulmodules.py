# Biblioteca math - https://docs.python.org/3/library/math.html

import math
math.sqrt() #Return the square root of x.
math.sin() #seno
math.cos() #coseno
math.log(x, base)
math.e #The mathematical constant e = 2.718281…, to available precision.

#Biblioteca Datetime - https://docs.python.org/3/library/datetime.html
import datetime
dir(datetime) #mostra as ooções de recursos da biblioteca
datetime.date.today() #dia atual

#Biblioteca random - https://docs.python.org/3/library/random.html
import random  #utilizada para gerar números aleatorios

#Biblioteca time - https://docs.python.org/3/library/time.html
import time as tm
antes = tm.time()
lista = []
for i in range (0, 10000):
  lista.append(i)
depos = tm.time()

intervalo = depois - antes
print(f'Tempo: {intervalo} segundos')

