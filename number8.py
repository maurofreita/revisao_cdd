"""Faça um código que receba 4
números e realize a soma deles e a
média entre eles. e mostre os
resultados."""

soma = 0

for x in range (4):
    num = int(input('Digite um número: '))
    soma = soma + num
media = soma / 2

print(f'A soma dos seus números foi {soma} e a média deles é {media}')
