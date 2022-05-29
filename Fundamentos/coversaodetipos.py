a = 2 + '3' #Resultado é um erro pois não se pode fazer a soma nem concatenação de tipos diferentes

b = 2
c = '3'

print(a + int(b)) #A função modifica o tipo da variável b para inteiro só funciona se a string for numérica inteira.
print(str(a) + b) #Modifica o a para string