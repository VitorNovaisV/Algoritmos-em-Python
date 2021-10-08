from datetime import date


def voto(nas):
    anoat = date.today().year
    idade = anoat - nas
    if idade <16:
        print(f'Com {idade} anos não se Vota.')
    elif 16 <= idade < 18 or idade > 65:
        print(f'Com {idade} anos Votar é Opcional.')
    elif idade >18:
        print(f'com {idade} anos Voto é Obrigatório')


voto(1910)
