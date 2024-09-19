a = int(input())
b = int(input())

digits = [int(d) for d in str(a) + str(b)]

max_digit = max(digits)
min_digit = min(digits)

digits.remove(max_digit)
digits.remove(min_digit)

middle_digit = sum(digits) % 10

magic_number = max_digit * 100 + middle_digit * 10 + min_digit

print(magic_number)