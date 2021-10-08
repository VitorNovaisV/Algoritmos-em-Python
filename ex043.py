print('Calculador de IMC: ')
peso = float(input('Qual é o seu peso? (KG): '))
altura = float(input('Qual é sua altura? (m): '))
imc = peso / (altura ** 2)
print(f' o IMC dessa pessoa é de {imc:.1f}')
if imc < 18.5:
    print('Abaixo do peso normal')
elif 18 <= imc < 25:
    print('Peso Normal')
elif 25 <= imc < 30:
    print('Sobrepeso')
elif 30 <= imc <40:
    print('Obesidade')
elif imc >= 40:
    print('Obesidade Mórbida')
