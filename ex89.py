ficha = []
while True:
    nome = str(input('Nome do Aluno: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar?[S/N]: ')).strip().lower()
    while resp not in 'sn':
        resp = str(input('Quer continuar?, RESPONDE DIREITO!!![S/N]: ')).strip().lower()
    if resp in 'n':
        break
print('=-'*30)
print(f'{"No.":<4}{"Nome":<10}{"média":>8}')
print('=-'*30)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-' * 35)
    opc = int(input('Mostar notas de qual aluno? [999 para parar]: '))
    if opc == 999:
        print('Finalizando...')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc] [0]} são {ficha[opc][1]}')
print('=-'*30)