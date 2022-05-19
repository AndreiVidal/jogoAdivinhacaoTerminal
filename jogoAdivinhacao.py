from getpass import getpass


secreta = getpass('Digite uma palavra secreta: ')
tamanho = len(secreta)
digitadas = list()
chances = len(secreta) - 2
indice = print(f'A palavra secreta tem {tamanho} letras.')


while True:
    if chances <= 0:
        print(f'Voçê PERDEU!!')
        break

    letra = input('Digite uma letra: ')

    if letra == secreta:
        print(f'A palavra é: {secreta}')
        print('PARABÉNS!! Voçê venceu.')
        break
    elif len(letra) > 1:
        print('Digite apenas uma letra')
        continue

    digitadas.append(letra)

    if letra in secreta:
        print(f'A letra "{letra}" está na palavra!')
    elif letra.isnumeric():
        print('Digite apenas letras:')
    else:
        print(f'A letra {letra} não está na palavra!')
        digitadas.pop()

    secreto_temporario = ''
    for letra_secreta in secreta:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'

    if secreto_temporario == secreta:
        print(f'Palavra: {secreta}')
        print('PARABÉNS!! Voçê venceu.')
        break
    else:
        print('=' * 25)
        print(f'Palavra secreta: {secreto_temporario}')

    if letra not in secreta:
        chances -= 1
    print('='*25)
    print(f'Voçê ainda tem {chances} chances')
    print('='*25)