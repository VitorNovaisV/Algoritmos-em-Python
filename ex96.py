def area(l, c):
    a = (l * c)
    print(f'A Área de {l} X {c} é {a}M²')


print('--Calculador de áreas--')
larg = float(input('Digite a Largura: '))
comp = float(input('Digite o Comprimento: '))
area(larg, comp)
