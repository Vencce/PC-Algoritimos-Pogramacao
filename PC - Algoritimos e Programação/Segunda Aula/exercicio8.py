dias = float(input('Quantos dias o carro foi alugado? '))
km = float(input('Quantos km foram percorridos? '))

total = (dias * 60) + (km * 0.15)

print('O total a pagar é de {}.'.format(total))