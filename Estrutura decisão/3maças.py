# Número de maças compradas

macas = int(input('Quantas macas foram compradas:'))

if macas < 12:
    custo_total = macas * 1.30
else:
    custo_total = macas * 1.00

print('O custo total da compra é: R$ {}'.format(custo_total))
