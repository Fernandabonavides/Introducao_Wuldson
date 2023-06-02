# Número da conta do cliente, saldo, débito e crédito

conta = int(input('Digite o numero da sua conta:'))
saldo = float(input('Digite o valor do saldo atual R$:'))
debito = float(input('Digite o valor do debito R$:'))
credito = float(input('Digite o valor do credito R$:'))

# Calcular se a conta está negativa ou positiva

saldo_atual = (saldo - debito + credito)
if saldo_atual >= 0:
    print('O saldo da conta{}, é de R$ {}, e é positivo'.format(conta, saldo_atual))

else:
    print('O saldo da conta{}, é R${}, e está negativo'.format(saldo, saldo_atual))

