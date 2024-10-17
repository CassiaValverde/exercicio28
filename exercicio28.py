#descontos progressivos
valor = float(input('Qual o valor a ser descontados ? \n'))
porcentagem = 100*0.05
porcentagem2 = 100*0.10

if valor >= 100 and valor <= 499:
 print(valor-porcentagem)
elif  valor >=  500:
 print(valor-porcentagem2)
else:
 print('Não tem desconto')
