import itertools


def sa(x1, y1, x2, y2, x3, y3):
    return ((x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1)) // 2


x = [0] * 4
y = [0] * 4
l = [0] * 4
for i in range(4):
    x[i], y[i] = map(int, input().split())
for i in range(4):
    l[i] = sa(x[i], y[i], x[(i + 1) % 4], y[(i + 1) %
                                            4], x[(i + 2) % 4], y[(i + 2) % 4])
res = True
for tup in itertools.combinations(l, 2):
    if tup[0] * tup[1] < 0:
        res = False
        break
print("Yes" if res else "No")
