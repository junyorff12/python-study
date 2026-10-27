
print('Jogo da palavra secreta')

palavra_secreta = 'avestruz'
letras_certas = ''



while True:
    letra_digitada = input('Digite uma letra:')

    if len(letra_digitada) > 1:
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







