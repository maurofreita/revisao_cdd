"""Escreva um algoritmo para ler o
número total de eleitores de um
município, o número de votos brancos,
nulos e válidos. Calcular e escrever o
percentual que cada um representa em
relação ao total de eleitores."""

eleitores = int(input("Digite o número de eleitores: "))
votos_brancos = int(input("Digite o número de votos brancos: "))
votos_nulos = int(input("Digite o número de votos nulos: "))
total_validos = int(input("Digite o número de votos validos: "))


porc_nul = (votos_nulos/eleitores)*100
porc_branco = (votos_brancos/eleitores)*100
porc_valido = (total_validos/eleitores)*100

print(f"A porcentagem de pessoas que votaram foi de : {eleitores}% ")
print(f"A porcentagem de votos nulos foi de: {porc_nul}% ")
print(f"A porcentagem de votos brancos foi de: {porc_branco}% ")
print(f"A porcentagem de votos validos foi de : {porc_valido}% ")
