# dados
cads = 1
mais18 = 0
home = 0
mulher20 = 0
naonas = 0
provded = 0
print('=-'*30)
print('CADASTRAMENTO')
print('=-'*30)
while True:
    gen = str(input('Gênero[M/F/O]: ')).strip().upper()
    while gen not in 'MFO':
        gen = str(input('Gênero[M/F/O]: ')).strip().upper()
    idade = int(input('Idade:'))
    resp = str(input('Quer continuar?[S/N]')).strip().upper()
    while resp not in 'SN':
        resp = str(input('Quer continuar?(RESPONDE CERTO![S/N]: ')).strip().upper()
        cads +=1
    if idade >= 18:
        mais18 +=1
    if gen =='M':
        home +=1
    if gen == 'F' and idade <=20:
        mulher20 +=1
    if idade <=1:
        naonas +=1
    if idade >150:
        provded +=1
    if resp =='N':
        break
print('=-'*30)
print(f'Você cadastrou {cads} Pessoas')
print(f'{mais18} Pessoas possuem mais de 18 anos')
print(f'{home} São Homens')
print(f'{mulher20} São Mulheres com menos de 20 Anos')
if naonas >0:
    print(f'{naonas} Não Nasceram ainda')
if provded >0:
    print(f'{provded} Provavelmente Estão Mortas.')
print('=-'*30)
