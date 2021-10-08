from time import sleep
from random import randint
def sorteia(lista):
    print('Sorteando 5 calores da lista: ', end='')
    for c in range(0,5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n} ', end='')
        sleep(0.4)
    print('Pronto')
def somapar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {lista}, temos {soma}')


# programa
numeros = list()
sorteia(numeros)
somapar(numeros)