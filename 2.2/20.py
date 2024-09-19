a = input()
b = input()
c = input()
arr = [x for x in [a, b, c] if 'зайка' in x]
print(min(arr), len(min(arr)))