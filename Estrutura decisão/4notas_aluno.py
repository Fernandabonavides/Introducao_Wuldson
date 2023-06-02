# Notas da 1ª e 2ª avaliação

Nota1 = float(input('Digite a nota 1:'))
Nota2 = float(input('Digite a nota 2:'))

# Calcular média simples e informar se foi aprovado ou não.

media = (Nota1 + Nota2) / 2
if media >= 6.0:
    print('Sua media foi {}. Parabéns, você foi aprovado'.format(media))

else:
    print('Sua media foi {}. Não foi dessa vez'.format(media))

