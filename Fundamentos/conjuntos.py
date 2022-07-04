#Conjunto não aceita repetições não é ordenado

a = {1, 2, 3}

print(type(a))

a = set('Coddddddd3r')#Separa cada elemento e cria um conjunto ignorando as repetições. 

print(a)

print('3' in a, 4 not in a)#Realiza operações de contem ou está contido, os elementos dentro do conjunto são strings.

print({1, 2, 3} == {3, 2, 1, 3})

c1 = {1, 2}
c2 = {2, 3}

print(c1.union(c2))#Realiza a união dos dois conjuntos informados.
print(c1.intersection(c2))#Mostra os elementos comuns nos dois conjuntos.

c1.update(c2)#Altera o primeiro conjunto com os elementos do segundo.