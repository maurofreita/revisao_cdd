"""Faça um algoritmo que leia a idade de
uma pessoa expressa em anos, meses e dias
e escreva a idade dessa pessoa expressa
apenas em dias. Considerar ano com 365
dias e mês com 30 dias."""

ano = int(input("Escreva sua idade: "))
mes = int(input("Escreva mês que você nasceu: "))
dia = int(input("Escreva o dia que você nasceu: "))

diatotal = (ano * 365) + (mes * 30) + dia

print(f"Sua idade em dias é: {diatotal} ")
