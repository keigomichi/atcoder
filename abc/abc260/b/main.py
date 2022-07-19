n, x, y, z = map(int, input().split())
l = [i for i in range(n)]
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = [v + w for v, w in zip(a, b)]
res = []
for _ in range(x):
    i = a.index(max(a))
    res.append(l.pop(i))
    a.pop(i)
    b.pop(i)
    c.pop(i)
for _ in range(y):
    i = b.index(max(b))
    res.append(l.pop(i))
    a.pop(i)
    b.pop(i)
    c.pop(i)
for _ in range(z):
    i = c.index(max(c))
    res.append(l.pop(i))
    a.pop(i)
    b.pop(i)
    c.pop(i)
for v in sorted(res):
    print(v + 1)
