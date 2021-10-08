p = float(input('Qual é o preço do produto? R$'))
d = float(p*5/100)
pd = float(p - d)
print(f'O produto custava R${p:.2f}, e com desconto de 5% vai custar R${pd:.2f}')

