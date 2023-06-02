# Tabuada que receba um número

numero = int(input('Digite um numero para saber a tabuada:'))

for i in range (1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")