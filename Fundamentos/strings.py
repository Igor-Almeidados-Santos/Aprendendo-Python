#Funções do tipo string.
print(dir(str))

nome = 'Pedro Paulo'
print(nome[0])#A string pode ser acessada por um indice.
print(nome[-3])#Acessa da direita pra esquerda começando do -1.
print(nome[4:])#Acessa a partir da posição 4 até o final.
print(nome[-3:])#Acessa da posição -1 até a -3.
print(nome[:3])#Vai da posição zero até dois.
print(nome[2:4])#Vai da posição 2 até a 3

numero = '123456789'
print(numero[::2])#Percorre Todas as posições da string e printa de 2 em 2.
print(numero[::-1])#Inverte a string.

#nome[0] = 'p' #Os indices da string não podem ser modificados.

#Texto de multipla linhas
texto1 = """texto com 
multiplas
linhas"""

texto2 = '''Texto 
com 
multiplas
linhas'''
print(texto1)
print(texto2)

frase = 'Amanhã vou lá hoje!'

print('am'in frase)#Considera-se a letra maiuscula então retorna um valor false.
print('vou lá'in frase)

print(len(frase))#tamanho da string
print(frase.lower())#transforma em lowercase sem transformar a variável original
print(frase.upper)#transforma em upercase sem transformar a variável original
print(frase.split())#Separa as palavras da frase
print(frase.split('v'))#quebra a partir de uma determinada letra