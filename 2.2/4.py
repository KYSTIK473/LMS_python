a = (int(input()), 'Петя')
b = (int(input()), 'Вася')
c = (int(input()), 'Толя')
arr = [a, b, c]
arr = list(sorted(arr))
for i in range(len(arr)):
    print(f'{i + 1}. {arr[-(i + 1)][1]}')