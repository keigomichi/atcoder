n = int(input())
s = sorted([list(map(int, input().split())) for _ in range(n)])
res = []
for l, r in s:
    if res == []:
        res.append([l, r])
    if res[-1][1] < l:
        res.append([l, r])
    else:
        res[-1][1] = max(res[-1][1], r)
for l, r in res:
    print(l, r)
