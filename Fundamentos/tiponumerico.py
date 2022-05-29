#Funções do tipo int:
print(dir(int))
print(dir(float))

#Operações com tipos numéricos

a = 5
b = 2.5

print(a / b)#Divisão comum sempre gera um número float mesmo os dois sendo inteiros.
print(a + b)#Soma de um número int e um float gera um resultado float e int + int gera um resultado int
print(a * b)#Multiplicação segue o princípio da soma.

#Verificar se um número float é inteiro(Casa decimal igual a 0):
print(b.is_integer())
print(5.0.is_integer())

#Trabalhando com decimais
print(1.1+ 2.2)#Gera um resultado impreciso por conta da especificação do float.

from decimal import Decimal, getcontext
print(Decimal(1) / Decimal(7))

getcontext().prec = 2#Muda a precisão de casas decimais do resultado.
print(Decimal(1) / Decimal(7))
print(Decimal.max(Decimal(1), Decimal(7)))#Retorna o maior entre os dois.
print(dir(Decimal))