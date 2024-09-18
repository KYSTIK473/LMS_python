product = input().strip()
price_per_kg = int(input().strip())
weight = int(input().strip())
money_given = int(input().strip())

total_price = price_per_kg * weight
change = money_given - total_price

print("================Чек================")
print(f"Товар:{product:>29}")
s = f'{weight}кг * {price_per_kg}руб/кг'
print(f"Цена:{s:>30}")
print(f"Итого:{total_price:>26}руб")
print(f"Внесено:{money_given:>24}руб")
print(f"Сдача:{change:>26}руб")
print("===================================")