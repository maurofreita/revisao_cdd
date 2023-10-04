""".As maçãs custam R$ 1,30 cada se forem
compradas menos de uma dúzia, e R$ 1,00
se forem compradas pelo menos 12. Escreva um
programa que leia o número de maçãs
compradas, calcule e escreva o custo total da compra."""

maca_comp = int(input("Informe quantas maçãs você comprou: "))

if maca_comp < 12:
    valor_total = maca_comp*1.30

else:
    valor_total = maca_comp*1.00

print(f"O valor da compra foi de  R${valor_total} ")