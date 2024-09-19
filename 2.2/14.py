a = list(map(int, list(input())))
a = list(sorted(a))
if a[0] == 0:
    print(f'{a[1]}{a[0]} {a[2]}{a[1]}')
else:
    print(f'{a[0]}{a[1]} {a[2]}{a[1]}')