
print('Jogo da palavra secreta')

palava_secreta = 'avestruz'
qtd_tentativas = 0
palavra_formatada = ''

for i in palava_secreta:
    palavra_formatada[i] = '*'

while True:
    letra = input('Digite uma letra:')
    for i in palava_secreta:
        if letra == i:
            print(letra)
        else: 
            print("*")    
    qtd_tentativas += 1

print(palavra_formatada)





