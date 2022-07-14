n = int(input())
a = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if j == 0 or i == j:
            a[i][j] = 1
        else:
            a[i][j] = a[i - 1][j - 1] + a[i - 1][j]
for i in range(n):
    print(*a[i][:i + 1])
