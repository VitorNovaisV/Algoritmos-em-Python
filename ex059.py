num1 = int(input('Digite um número: '))
num2 = int(input('Digite mais um número: '))
menu = 0
while menu !=5:
    print('escolha uma opção do menu:')
    menu=int(input('''
   [ 1 ]: para soma
   [ 2 ]: para multiplicar
   [ 3 ]: para ver qual e o maior
   [ 4 ]: para escolher novos numeros
   [ 5 ]: para sair do programa
    Digite aqui: '''))
    if menu == 1:
        op1 = num1 + num2
        print(f'a soma entre {num1} e {num2} é {op1}')
    if menu ==2:
        op2 = num1 * num2
        print(f'a multiplicação entre {num1} e {num2} é {op2}')
    if menu == 3:
        if num1 > num2:
            print(f'O Número maior é {num1}')
        elif num2 > num1:
            print(f'O Número maior é {num2}')
        else:
            print(f'Os valores {num1} e {num2} são iguais.')
    if menu == 4:
        num1 = int(input('Digite o novo 1° número: '))
        num2 = int(input('Digite o novo 2° número: '))
    if menu == 5:
        print('Finalizando...')
    if menu == 0 or menu <0 or menu >5:
        print('opção invalida')
print('End')


