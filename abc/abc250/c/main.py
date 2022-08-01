n, q = map(int, input().split())
d = {i + 1: i + 1 for i in range(n)}
print(d)
for _ in range(q):
    x = int(input())
    tmp = d[x]
    if d[x] != n:
        d[x] = d[x + 1]
        d[x + 1] = tmp
    else:
        d[x] = d[x - 1]
        d[x - 1] = tmp
    print(d)
print(d)