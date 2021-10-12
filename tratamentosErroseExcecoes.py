# NameError: variável não foi definida
# TypeError: tipos de dados incompatíveis 
# RuuntimeError: erro de execução 
# SyntaxError: somtaxe digitada é inválida e não reconhecida pelo interpretador 
# ZeroDivisionError: divisão por zero
# IndexError: índice está fopra da coleção
# ValueError: quando o numero digitado é diferente de número


#ex.:

try: 
  n = int(input('Digite um número inteiro: '))
except:
  print('Valor inválido')
else:
  print(f'Valor digitado é {n}')
  break
#dessa forma ele não vai apresentar um dos erros acima e vai tratar como uma exceção

while True:
  try:
    p = int(input(' Digite um número inteiro: ' ))
  except ValueError:
    print('Valor inválido')
  except KeyboardInterrupt:
    print('Usuário interrompeu a execução')
    break
  else:
    print(f'Valor digitado é {p}')
    break
    
    #são diferentes tipos de erros
    
