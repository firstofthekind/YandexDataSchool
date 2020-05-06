def inum(fib_str):
    num = ''
    for index, i in enumerate(fib_str):
        num = num + i
        if i == ' ' or index == len(fib_str) - 1:
            yield int(num)
            num = ''


def iflnum(fib_str):
    num = ''
    for index, i in enumerate(fib_str):
        num = num + i
        if i == ' ' or index == len(fib_str) - 1:
            yield float(num)
            num = ''

def init(lr):
    a = input()
    a = list(inum(a))
    b = 0
    c = a[1] - a[0] + 1
    while a[0] <= a[1]:
        b += 1 / float(ai[a[0]])
        a[0] += 1
    return round(c / b, 6)


n = input()
ai = list(iflnum(input()))
q = input()
lr = []
out = []
for i in range(int(q)):
    out.append(init(lr))
for i in out:
    print(i)
