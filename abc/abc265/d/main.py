n, p, q, r = map(int, input().split())
a = list(map(int, input().split()))
b = [0] * (n + 1)
for i in range(1, n + 1):
    b[i] = b[i - 1] + a[i - 1]
s = set(b)
for e in s:
    if e + p in s and e + p + q in s and e + p + q + r in s:
        print('Yes')
        exit()
print('No')
