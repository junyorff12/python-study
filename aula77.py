
print('Jogo da palavra secreta')

palavra_secreta = 'avestruz'
qtd_tentativas = 0
letras_certas = ''
palavra_formatada = ''

while True:
    letra = input("Digita uma letra: ")
    if len(letra) > 1:
        print('Digite somente uma letra:')
        continue
    if letra in palavra_secreta:
        letras_certas += letra

    if len(letras_certas) == len(palavra_secreta):
        






