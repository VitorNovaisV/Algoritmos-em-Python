from math import factorial
n = int(input('Digite um número para calcular o seu fatorial: '))
c = n
print(f'Calculando {n}!:')
while c > 0:
    print(f'{c}',end='')
    print(' x ' if c > 1 else ' = ',end='')
    c -= 1
print(f'{factorial(n)}')
