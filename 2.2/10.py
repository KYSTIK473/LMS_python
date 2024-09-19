# Чтение трехзначного числа
number = input().strip()

# Извлечение цифр
hundreds = int(number[0])
tens = int(number[1])
units = int(number[2])

# Суммы цифр
sum_1 = tens + units  # Сумма десятков и единиц
sum_2 = hundreds + tens  # Сумма сотен и десятков

# Формирование нового числа в порядке не возрастания
result = f"{max(sum_1, sum_2)}{min(sum_1, sum_2)}"

# Вывод результата
print(result)