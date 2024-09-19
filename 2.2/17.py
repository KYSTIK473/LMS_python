import math

a = float(input())
b = float(input())
c = float(input())

discriminant = b ** 2 - 4 * a * c

if a == 0:
    if b == 0:
        if c == 0:
            print("Infinite solutions")
        else:
            print("No solution")
    else:
        print(-c / b)
elif discriminant < 0:
    print("No solution")
elif discriminant == 0:
    print(-b / (2 * a))
else:
    x1 = (-b + math.sqrt(discriminant)) / (2 * a)
    x2 = (-b - math.sqrt(discriminant)) / (2 * a)
    print("{:.2f} {:.2f}".format(min(x1, x2), max(x1, x2)))
