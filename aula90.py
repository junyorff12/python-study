#enumerate

t = ('jr', 'ff', '12')

enum = list(enumerate(t))

print(enum)

n = enumerate(t)

for i, v in n:
    print(i, v)