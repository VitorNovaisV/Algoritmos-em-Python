d = float(input('Qual a Distancia que Você pretende viajar em km?: '))
v1 = d * 0.50
v2 = d * 0.45
print('O Valor da sua viagem foi: ')
if d < 200:
    print(f'R${v1:.2f}')
else:
    print(f'R${v2:.2f}, Viagens Acima de 200km possuem Desconto!')
print('Tenha Uma Boa Viagem!!')
