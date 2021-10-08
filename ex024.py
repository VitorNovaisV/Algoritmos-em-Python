#024: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".
city = str(input('Digite um nome de uma cidade: '))
c1 = city.strip()
c2 = c1.lower()
print (f'A cidade tem a palavra "Santo"?: {"santo"in c2} ')
