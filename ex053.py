print('\033[34mDetector de Palídromo\033[m')
a = str(input('Digite Uma frase: ')).strip().upper()
b = a.split()
frase1 = ''.join(b)
print(f'O Inverso de {frase1} é {frase1 [::-1]}.')
if frase1 == (frase1[::-1]):
    print('Temos um Palíndromo!')
