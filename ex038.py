pri = int(input('Digite o Primeiro número: '))
seg = int(input('Digite o Segundo número: '))
if (pri < seg):
    print('O Segundo número é maior')
elif (seg < pri):
    print('O Primeiro número é maior')
elif (pri == seg):
    print('Os Números são Iguais!')