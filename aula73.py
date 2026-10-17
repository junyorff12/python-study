#for

texto = 'python'
nova_texto = ''

for letra in texto:
    nova_texto += f'*{letra}'
    print(letra)
print(nova_texto) # pyright: ignore[reportUndefinedVariable]