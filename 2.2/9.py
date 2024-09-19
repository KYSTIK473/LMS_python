# Чтение имен игроков из ввода
players = [input().strip() for _ in range(3)]

# Определение имени игрока с лексикографически меньшим именем
first_player = min(players)

# Вывод имени первого игрока
print(first_player)