n = input()
lista = input()
listb = lista.split()
newlist = []
i=0
res = list(dict.fromkeys(listb))
print(len(res))
print(res)
print(' '.join(res))
