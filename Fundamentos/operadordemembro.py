#Operador de Membro
from re import X


lista = [1, 2 , 3, 'Ana', 'Jana']
print(1 in lista)# Verifica se o membro 1 está na lista
print('Ana' not in lista)# Verifica se o membro Ana não está na lista

#Operador de Identidade
x = 3
y = x
z = 3
#Verifica se o valor da comparação é igual.
print('________________')
print(x is y)
print(y is z)
print(x is not z)

lista_a = [1, 2, 3]
lista_b = lista_a
lista_c = [1, 2, 3]

print('________________')
#Listas apontam para um espaço de memória por isso mesmo que os valores de lista_a e lista_c são iguais eles apontam pra registros diferentes.
print(lista_a is lista_b)
print(lista_b is lista_c)
