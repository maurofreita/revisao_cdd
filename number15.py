"""Escreva um algoritmo para ler dois
valores (considere que não serão lidos
valores iguais) e escrevê-los em ordem
crescente"""

num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))
while num1 == num2:
    num2 = int(input("Número igual, digite um número diferente: "))

if num1 < num2:
    print(num1, num2)
else:
    print(num2, num1)
