n, x = map(int, input().split())
res = 100000000000000000000
min_b = 10000000000
s = 0
for i in range(1, n + 1):
    a, b = map(int, input().split())
    s += a + b
    min_b = min(b, min_b)
    res = min(res, s + min_b * max(0, x - i))
print(res)
