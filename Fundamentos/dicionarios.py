#Dicionário é uma estrutura de chave e valor

pessoa = {
    'nome': 'prof(a) Ana',
    'idade': 38,
    'cursos': ['Inglês', 'Portugês']
}

print(type(pessoa))
print(dir(dict))

print(pessoa.keys())#Mostra o nome das chaves do dicionário.
print(pessoa.values())#mostra os Valores do dicionário.
print(pessoa.items())#Mostra os as chaves e valores.
print(pessoa.get('tags', []))#Se não encontrar o primeiro elemento informado retorna um array vazio.

pessoa['cursos'].append('Francês')#Adiciona novo elemento em uma chave.

pessoa.pop('idade')#Retira a chave e o valor relacionado a ela
pessoa.update({'Sexo':'M', 'idade': 45})

del pessoa['cursos']#Exclui a chave e o valor relacionado.

pessoa.clear()#Limpa o dicionário

print(pessoa)