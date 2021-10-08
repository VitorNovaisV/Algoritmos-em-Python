# Escreva um programa para aprovar o empréstimo  bancário para a compra
# de uma casa. Pergunte o valor da casa, o salário do comprador e em
# quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário
# ou então o empréstimo será negado.
print('=-' * 24)
casa = float(input('Valor da casa: R$'))
salario = float(input('Valor do Sálario mensal: '))
anos = int(input('Quantos anos serão de financiamento?: '))
prest = casa / (anos * 12)
min = salario * 30 /100
print(f'Para pagar uma casa de R${casa:.2f}, em {anos} Anos.')
print(f'A prestação será de R${prest:.2f}')
if prest <= min:
    print('\033[1;32mEmpréstimo Consedido!\033[m')
else:
    print('\033[1;31mEmpréstimo Negado.\033[m')
print('=-' * 24)
