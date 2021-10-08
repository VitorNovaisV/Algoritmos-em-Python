aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['media'] >= 7:
    aluno['situação'] = 'Aprovado'
elif aluno['media'] < 6:
    aluno['situação'] = 'Reprovado'
else:
    aluno['situação'] = 'Recuperação'
for key, value in aluno.items():
    print(f'{key}: ', value)
