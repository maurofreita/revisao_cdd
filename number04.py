"""Crie um algoritmo que receba 3
números e informe qual o maior entre
eles."""

num_1 = int(input('Digite um número: '))
num_2 = int(input('Digite mais um número: '))
num_3 = int(input('Digite o último número: '))

if num_1 > num_2:
    if num_1 > num_3:
        print(f'O {num_1} é o maior.')
    else:
        print(f'O {num_3} é o maior.')
elif num_2 > num_3:
    print(f'O {num_2} é o maior.')
else:
    print(f'O {num_3} é o maior.')
