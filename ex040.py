print('Digite as Notas do Aluno: ')
n1 = float(input('Primeira Nota: '))
n2 = float(input('Segunda Nota: '))
m = ((n1 + n2) / 2)
print(f'A Nota Final do aluno foi: {m:.1f}.')
if m <= 4.9:
    print('O Aluno foi REPROVADO.')
elif m >= 4.9 and m <= 6.9:
    print('Aluno em RECUPERAÇÃO.')
elif m >= 7.0 and m <= 10.0:
    print('Aluno APROVADO.')
else:
    print('Nota Invalida')

