purchase_price_bin = input()
cash_given = int(input())

purchase_price = int(purchase_price_bin, 2)
change = cash_given - purchase_price

print(change)