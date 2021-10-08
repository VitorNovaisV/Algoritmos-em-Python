from random import randint
n = (randint(1, 10),
     randint(1, 10),
     randint(1, 10),
     randint(1, 10),
     randint(1, 10))
print(f'Sorteei os Valores: {n}')
print(f'O Maior Valor Sorteado foi {max(n)}')
print(f' O Menor Valor Sorteado foi {min(n)}')

