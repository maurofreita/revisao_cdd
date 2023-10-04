"""Crie um código que leia um número
diferente de zero e diga se este número
é positivo ou negativo. """


num = int(input('Digite um número que não seja 0: '))

while num == 0:
    num = int(input('O número não pode ser 0, digite novamente: '))

if num > 0:
    print('Seu número é positivo.')

else:
    print('Seu número é negativo.')
