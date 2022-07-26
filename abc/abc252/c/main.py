n = int(input())
s = [input() for _ in range(n)]
l = []
for i in range(10):
    d = dict()
    for t in s:
        w = t.index(str(i))
        if w not in d:
            d[w] = 0
        else:
            d[w] += 1
    k, v = max([kv for kv in d.items() if kv[1] == max(d.values())])
    l.append(v * 10 + k)
print(min(l))
