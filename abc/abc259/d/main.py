def intersects(c1x, c1y, r1, c2x, c2y, r2):
    d = ((c1x - c2x) ** 2 + (c1y - c2y) ** 2) ** 0.5  # **0.5不要
    return d < r1 + r2


n = int(input())
sx, sy, tx, ty = map(int, input().split())
x = [0] * n
y = [0] * n
r = [0] * n
for i in range(n):
    x[i], y[i], r[i] = map(int, input().split())

for i in range(n):
    if (x[i] - sx) ** 2 + (y[i] - sy) ** 2 == r[i] ** 2:
        si = i
    if (x[i] - tx) ** 2 + (y[i] - ty) ** 2 == r[i] ** 2:
        ti = i

for i in range(n - 1):
    for j in range(i + 1, n):
        if intersects(x[i], y[i], r[i], x[j], y[j], r[j]):
            pass