a = (int(input()), 'Петя')
b = (int(input()), 'Вася')
c = (int(input()), 'Толя')
s = ''
arr = [a, b, c]
arr = list(sorted(arr))[-1::-1]
print(f"{arr[0][1]:^24}")
print("{:^8}".format(arr[1][1]))
print("{:>22}".format(arr[2][1]))
a1 = 'II'
a2 = 'I'
a3 = 'III'
print(f"{a1:^8}{a2:^8}{a3:^8}")