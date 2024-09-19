import math

a = int(input())
b = int(input())
c = int(input())
arr = list(sorted([a, b, c]))
# Проверка на существование треугольника
if a + b > c and a + c > b and b + c > a:

    gr = max(arr) ** 2

    grmin = list(map(lambda x: x ** 2, arr))
    gm = sum(grmin) - gr

    if gr < gm:
        print("крайне мала")
    elif gr == gm:
        print("100%")
    else:
        print("велика")
else:
    print("Невозможно определить вероятность. Введенные данные не образуют треугольник.")
