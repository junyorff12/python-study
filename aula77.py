import os
import sys

def limpar_terminal() -> None:
    if sys.platform == 'linux' or sys.platform == 'darwin':
        os.system('clear')
    elif sys.platform == 'win32':
        os.system('cls')


print('Jogo da palavra secreta')

palavra_secreta = 'avestruz'
letras_certas = ''
quantidade_tentativas = 0

while True:
    quantidade_tentativas += 1
    letra_digitada = input('Digite uma letra:')

    if len(letra_digitada) != 1:
        print('Digite somente uma letra.')
        continue

    if letra_digitada in palavra_secreta:
        letras_certas += letra_digitada
    
    palavra_formatada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_certas:
            palavra_formatada += letra_secreta
        else:
            palavra_formatada += '*'
    print(palavra_formatada)

    if palavra_formatada == palavra_secreta:
        limpar_terminal()

        print('Você acertou!!!!!!!!!!!')
        print(f'A palavra é: {palavra_secreta}')
        print(f'Quantidade de tentativas: {quantidade_tentativas}')
        letras_certas = ''
        quantidade_tentativas = 0
        res = input("Jogar novamente? sim/nao")
        if res == 'sim':
            continue
        else:
            limpar_terminal()
            print('tchau!')
            break






