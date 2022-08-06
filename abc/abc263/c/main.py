n, m = map(int, input().split())
v = [[] for _ in range(m + 1)]
for i in range(1, m + 1):
    v[1].append([i])
for i in range(1, n):
    for x in v[i]:
        b = x[-1] + 1
        for a in range(b, m + 1):
            y = x + [a]
            v[i + 1].append(y)
print(v)
for w in v[n]:
    print(*w, end=' \n')
