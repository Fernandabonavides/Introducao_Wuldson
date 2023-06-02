# Digitar altura do homem e da mulher

alturah = float(input('Digite a altura do homem:'))
alturam = float(input('Digite a altura da mulher:'))

# Formulas para homem e para mulher

homem =  (72.7 * alturah) - 58
mulher =  (62.1 * alturam) - 44.7

# Peso ideal

print('O peso ideal para o homem é: {}, e para a mulher é: {}' .format(homem, mulher))

