#Escreva um programa em Python que leia um número inteiro qualquer
# e peça para o usuário escolher qual será a base de conversão:
# 1 para binário, 2 para octal e 3 para hexadecimal.
n = int(input('Digite um número inteiro: '))
v = int(input(' \033[0;34mDigite [ 1 ] para converter para BINÁRIO. \n Digite [ 2 ] para converter para OCTAL. \n Digite [ 3 ] para converter para HEXADECIMAL.: \033[m'))
if v == 1:
    print(f'O valor {n} em \033[34mBinário\033[m é: {bin(n)[2:]}')
elif v == 2:
    print(f'O valor {n} em \033[34mOctal é\033[m: {oct(n)[2:]}')
elif v == 3:
    print(f'O valor {n} em \033[34mHexadecimal\033[m é: {hex(n)[2:]}')
else:
    print('\033[0;31mERRO!\033[m Tente novamente selecionando uma das opções!')

