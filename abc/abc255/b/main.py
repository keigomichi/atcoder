from math import sqrt
n, k = map(int, input().split())
a = list(map(int, input().split()))
s = []
t = []
for i in range(n):
    x, y = map(int, input().split())
    if i + 1 in a:
        s.append([x, y])
    else:
        t.append([x, y])
ma = 0
for v in t:
    mi = 100000000000
    for w in s:
        dist = (v[0] - w[0]) ** 2 + (v[1] - w[1]) ** 2
        mi = min(mi, dist)
    ma = max(ma, mi)
print(sqrt(ma))
