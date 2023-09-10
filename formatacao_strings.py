# Utilizar o f antes da string permite voce habilitar
# a entrada de variaveis no texto

nome = 'Lucas Borges'
altura = 1.83
peso = 86
imc = peso / altura ** 2

linha_1 = f'{nome} tem {altura:.2f} de altura'
linha_2 = f'pesa {peso:.2f} quilos e seu imc é'
linha_3 = f'{imc:.2f}'

print (linha_1)
print (linha_2)
print (linha_3)