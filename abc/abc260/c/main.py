n, x, y = map(int, input().split())
r = [0] * n
b = [0] * n
r[0], b[0] = 0, 1
for i in range(1, n):
    b[i] = r[i - 1] + b[i - 1] * y
    r[i] = r[i - 1] + b[i] * x
print(r[n - 1])
