# Quantidade atual em estoque, quantidade máxima em estoque e quantidade mínima em estoque de um produto.

atual = int(input('Digite a quantidade atual em estoque:'))
maxima = int(input('DIgite a quantidade maxima em estoque:'))
minima = int(input('Digite a quantidade minima em estoque:'))

# Calcular e escrever a quantidade média ((quantidade média = quantidade máxima + quantidade mínima)/2).

media = (maxima + minima)/ 2
if atual >= media:
    print('Não efetuar a compra')

else:
    print('Pode efetuar a compra')

