N = int(input())
M = int(input())
T = int(input())

# Общее количество минут с начала суток
total_minutes = N * 60 + M + T

# Вычисляем новое время
new_hours = (total_minutes // 60) % 24
new_minutes = total_minutes % 60

# Форматируем результат
print(f"{new_hours:02}:{new_minutes:02}")