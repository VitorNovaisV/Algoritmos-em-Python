print('=-'*30)
print('Análisador de Expressões')
print('=-'*30)
expr = str(input('Dígite a Expressão:'))
aa = expr.cont('(')
bb = expr.cont(')')
if aa == bb :
    print('Sua Expressão é válida!')
else:
    print('Sua Expressão não é válida!')