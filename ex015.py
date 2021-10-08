dias = float(input('Quantos Dias ele foi Alugado?: '))
km = float(input('Quantos Km o Veículo percorreu?: '))
pd = dias*60.00
pkm = km*0.15
v = pd+pkm
print(f'O total a pagar é de R${v:.2f}')

