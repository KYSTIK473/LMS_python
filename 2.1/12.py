num1 = input().strip()
num2 = input().strip()

result = ''
length = max(len(num1), len(num2))

# Дополняем числа нулями слева
num1 = num1.zfill(length)
num2 = num2.zfill(length)

for digit1, digit2 in zip(num1, num2):
    result += str((int(digit1) + int(digit2)) % 10)

print(result)