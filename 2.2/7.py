def is_pal(a):
    if len(a) % 2 == 0:
        return a[:len(a) // 2] == (a[len(a) // 2:])[-1::-1]
    return a[:len(a) // 2] == (a[len(a) // 2 + 1:])[-1::-1]


if is_pal(input()):
    print('YES')
else:
    print('NO')
