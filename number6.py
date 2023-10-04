"""Ler um valor e escrever a mensagem É MAIOR
QUE 10! se o valor lido for maior que 10, caso
contrário escrever NÃO É MAIOR QUE 10!"""

num = int(input('Digite um número: '))

if num == 10:
    print('Seu número é 10.')
elif num > 10:
    print('Seu número é maior que 10!')
else:
    print('Seu número é menor que 10!')
