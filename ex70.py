total = maismil = maisba = quant = 0
while True:
    produto = str(input('Nome do Produto: '))
    preco = float(input('Valor do Produto: R$'))
    resp = str(input('Você Quer continuar? [S/N]')).strip().upper()
    if resp not in 'NS':
         resp = str(input('Você Quer continuar? [S/N]')).strip().upper()
    quant += 1
    total += preco
    if preco >= 1000:
        maismil += 1
    if quant == 1 or preco < maisba:
        maisba = preco
        maisba2 = produto
    if resp in 'N':
        break
print(f'Você registrou {quant} produtos\nO total foi de R${total:.2f}\n{maismil} Produtos custam mais de mil reais\nO produto mais barato foi {maisba2} e custou R${maisba:.2f} ')