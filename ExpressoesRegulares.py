#Expressões regulares - METACARACTERES

#.- Qualquer caractere(exceto linha nova)
#\w - Qualquer caractere alfanumérico
#\W - qualquer caractere não-alfanúmerico
#\d - qualquer caractere que seja um dígito(0-9)
#\D - Qualquer caractere não dígito
#\s - Espaço em braco
#^ - começa com
#$ - termina com
#"\" - usado antes de metacaracteres para especificar seu significado literal


#Expressões regulares - QUANTIFICADORES

#[] - Opcional entre os que estão dentro dos colchetes
#() - captura grupos de caracters
#* - de zero a mais vezes
#? - zero ou uma
#+ uma ou mais vezes
#{m,n} - de m a n vezes
#| or

#para procurar um e-mail ex: 

#vic.gabriella.c@gmail.com

#\w+@+\w+\.w+

# re = Regular Expression
#achar telefone em uma frase
import re

frase= 'Ola, meu telefone é (11)9000-1234'

re.search('\(\d{2\}\d{4,5}-\d{4}',frase)

# ------------------------------------
#achar a placa de um carro
import re

placa = " A placa do carro é SPN-2004'
re.search('[A-Za-z]{3}-\d{4}' , placa)

# ----------------------------------
# achar um e-mail 
import re
email = 'Meu e-mail e vic.gabriella.c@gmail.com'
re.search('\w+@\w+\.\w+',email)


# ----------------------------------

# Função Match

import re

placa = 'A placa do carro é SPN-2004' #não vai localizar pois não está no inicio da frase
placa2 = 'SPN-2004 é a placa do carro'
print(re.math('[A-Za-z]{3}-\d{4}' , placa2))


# ----------------------------------
# Função findall

frase3 = 'Ola, meu telefone é (11)9000-1234. O número antigo de telefone é (99)0000-0000'

re.findall('\(\d{2\}\d{4,5}-\d{4}',frase3) #retorna tudo o que for localizado em um arquivo 

#---
emails = 'vic.gabriella.c@gmail.com', 'vic.c@gmail.com.br', 'vic.gabriella@yahoo.com'
re.search('\w+@\w+\.\w*',emails)

