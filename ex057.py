sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Dados Inválidos,Informe seu sexo: [M/F] ')).strip().upper()[0]
if sexo == 'M':
    sex = 'Masculino'
elif sexo == 'F':
    sex = 'Feminino'
print(f'Sexo "{sex}" Definido Com Sucesso ')
