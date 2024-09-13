s = input()
a = int(input())
b = int(input())
c = int(input())
print(f"""Чек
{s} - {b}кг - {a}руб/кг
Итого: {a * b}руб
Внесено: {c}руб
Сдача: {c - a * b}руб
""")