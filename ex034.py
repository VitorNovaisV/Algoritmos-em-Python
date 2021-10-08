salario = float(input('qual o seu salário atual?: R$'))
if salario <=1250.00:
    aum = float(salario * 15/100)
else:
    aum = float(salario * 10/100)
print(f'O Seu Salário de R${salario} agora será de R${salario + aum:.2f}')