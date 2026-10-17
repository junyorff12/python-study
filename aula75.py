
texto = iter('Antonio')

iterator = iter('Antonio')

print(texto.__next__())
print(texto.__next__())
print(texto.__next__())
print(texto.__next__())
print(texto.__next__())
print(texto.__next__())
print(texto.__next__())

# usando while

while True:
    try:
        letra = next(iterator)
        print(f'letra {letra}')
    except StopIteration:
        break