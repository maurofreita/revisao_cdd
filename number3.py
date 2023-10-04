"""Crie um código que leia a idade de
uma pessoa e diga em qual ano ela
nasceu."""

idade = int(input('Digite sua idade: '))
ano = int(input('Digite o ano atual: '))
mes_atual = int(input('Digite em número o mês atual: '))
mes_nascido = int(input('Digite o mês que você nasceu: '))

if mes_atual == mes_nascido:
    nascido = ano - idade - 1
else:
    nascido = ano - idade

print(f'Você nasceu em {nascido}')


