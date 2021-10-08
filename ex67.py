while True:
    num = int(input('Digite um número para ver sua tabuada\n[Digite um número negativo para parar]:   '))
    if num < 0:
        break
    print('=-'*30)
    for c in range(1, 11):
        print(f'{num} x {c} = {num*c}')
    print('=-'*30)
print('Programa encerrado')
