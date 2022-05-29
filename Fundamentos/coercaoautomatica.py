#Toda divisão comum gera um resultado do tipo float.
print(10/2, type(10/2))
print(10/3, type(10/3))

#A divisão com duas barras pode gerar um valor inteiro ou float.
#Operações inteiro inteiro pode gerar tanto inteiro quanto float.
print(10//3, type(10//3))
print(10//2, type(10//2))

#Operações inteiro float sempre geram um float.
print(10//2.2, type(10//2.2))
print(10//3.3, type(10//3.3))