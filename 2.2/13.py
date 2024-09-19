# Чтение входных данных
numbers = [input().strip() for _ in range(3)]

# Поиск общей цифры в одинаковой позиции
for i in range(2):
    if numbers[0][i] == numbers[1][i] == numbers[2][i]:
        print(numbers[0][i])
        break