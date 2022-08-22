n, m, t = map(int, input().split())
a = list(map(int, input().split()))
b = [0] * n
for _ in range(m):
    x, y = map(int, input().split())
    b[x - 1] = y
for i in range(n - 1):
    t += b[i]
    t -= a[i]
    if t <= 0:
        print('No')
        exit()
print('Yes')
