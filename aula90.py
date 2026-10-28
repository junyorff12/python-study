#enumerate

t = ('jr', 'ff', '12')

enum = list(enumerate(t))

print(enum)

n = enumerate(t)

for i in n:
    print(i[0], type(i))