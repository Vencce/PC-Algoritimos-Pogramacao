preco_mercadoria = float(input('Qual o valor da mercadoria? '))
desconto = float(input('Qual o percentual de desconto? '))

desconto = (preco_mercadoria * desconto) / 100
valor_a_pagar = (preco_mercadoria - desconto)

print('O valor do desconto é {} e o valor a ser pago é {}.'.format(desconto, valor_a_pagar))