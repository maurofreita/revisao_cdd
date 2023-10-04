"""Escreva um algoritmo para ler a hora de
início e a hora de fim de um jogo de Xadrez
(considere apenas horas inteiras, sem os
minutos) e calcule a duração do jogo em
horas, sabendo-se que o tempo máximo de
duração do jogo é de 24 horas e que o jogo
pode iniciar em um dia e terminar no dia
seguinte"""

hora_inicio = int(input("Qual a hora de inicio: "))
hora_fim = int(input("Qual a hora de término: "))

if hora_inicio >= hora_fim:
    duracao = 24 - hora_inicio+hora_fim
else:
    duracao = hora_fim-hora_inicio

print(f"A duração do jogo foi de {duracao} horas")
