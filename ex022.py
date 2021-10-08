#022: Crie um programa que leia o nome completo de uma pessoa e mostre:
# - O nome com todas as letras maiúsculas e minúsculas.
# - Quantas letras ao todo sem considerar espaços.
#  - Quantas letras tem o primeiro nome.

n = str(input('Digite o seu o nome completo:'))
nome= n.strip()
nomemax = nome.upper()
nomemin = nome.lower()
print (str(f'O Seu nome Completo é {nome}'))
print (str(f'O Seu nome Completo apenas em Maiúsculas é: {nomemax}'))
print (str(f'O seu nome Completo apeans em Minúsculas é: {nomemin}'))
nome2 = nome.split()
print(f'esse nome tem {len("".join(nome2))} letras')
print(f'seu primeiro nome tem {len(nome2[0])} Letras')









