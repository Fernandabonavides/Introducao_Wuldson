# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.1. C = 5 * ((F-32) / 9).

tfah = float(input('Digite a temperatura:ºF'))

# Converta em graus Celsius com a fórmula C = 5 * ((F-32) / 9).

C = 5 * ((tfah-32) / 9)

# Exibindo temperatura em Celsius

print('A temperatura em graus Celsius é {}'.format(C))

