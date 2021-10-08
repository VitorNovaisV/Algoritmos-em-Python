import math
v = int(input('Qual é a Velocidade do Veículo em KM/H?: '))
limite = 80
m = (v - limite) * 7.00
if v >limite:
    print(f'Você ultrapassou o Limite de Velocidade de 80KM/H,Sua multa sera de R${m:.2f}')
print('Dirija com segurança, e tenha um bom dia.')
