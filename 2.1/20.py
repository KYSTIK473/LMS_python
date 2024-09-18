N = int(input().strip())
M = int(input().strip())
K1 = int(input().strip())
K2 = int(input().strip())
s = N * M
# Обозначим веса первой и второй партий
for w1 in range(N):
    if (w1 * K1 + (N - w1) * K2) == s:
        print(w1, N - w1)
        break
