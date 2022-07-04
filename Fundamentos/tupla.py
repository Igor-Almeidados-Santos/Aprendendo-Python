#Uma lista de elementos indexados não mutáveis.

tupla = tuple()#Pode-se criar apenas com "()"
print(dir(tupla))

tupla = ('un',)#Para criar a tupla com o parênteses e um unico elemento deve-se colocar a virgula no final.

print(tupla.index('un'))#Mostra o index do elemento dinformado.
print(tupla.count('un'))#Mostra a quantidade de elementos iguais existe na tupla.
print(len(tupla))#Mostra o tamanho da tupla.