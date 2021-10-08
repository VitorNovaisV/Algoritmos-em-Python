print(f'{"-=" * 11} Loja De Coisas!! {"-=" * 11}')
v = float(input('Valor Das Compras: R$'))
print('Formas de Pagamento:')
p = int(input("""[ 1 ] à vista dinheiro/cheque.
[ 2 ] à vista cartão.
[ 3 ] 2x no cartão.
[ 4 ] 3x ou mais no cartão.
: """))
if p == 1:
    print(f'a sua compra de R${v:.2f} vai custar R${v - (v * 10 / 100):.2f}')
if p == 2:
    print(f'a sua compra de R${v:.2f} vai custar R${v - (v * 5 / 100):.2f}')
if p == 3:
    print(f'a sua compra de R${v:.2f} em 2 parcelas de R${v / 2:.2f} terá um valor total de R${v:.2f} ')
if p == 4:
    x = int(input('Quantas Parcelas?: '))
    pp = float(v+ (v * x / 100))
    pp2 = float((pp / x))
    print(f'a sua compra de R${v:.2f} em {x} parcelas de R${pp2:.2f} tará um valor total de R${v + (v * x / 100):.2f}')