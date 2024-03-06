salario = int(input('Qual o valor do seu salário? '))
aumento = int(input('Qual a porcentagem de aumento? '))

aumento = (salario * aumento) / 100
novo_salario = (salario + aumento)

print('O valor do aumento é {} e o novo salário é {}.'.format(aumento, novo_salario))