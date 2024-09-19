number = input().strip()

# Извлечение цифр
digits = [int(d) for d in number]

# Определение минимальной и максимальной цифр
min_digit = min(digits)
max_digit = max(digits)

# Определение оставшейся цифры
remaining_digit = sum(digits) - min_digit - max_digit

# Проверка условия
if min_digit + max_digit == remaining_digit * 2:
    print("YES")
else:
    print("NO")