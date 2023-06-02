# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

hora = float(input('Quanto vc ganha por hora: R$'))
hmes = int(input('Quantas horas trabalha por mês:'))
salario = (hora * hmes)
print('O valor do salário é {}'.format(salario))
