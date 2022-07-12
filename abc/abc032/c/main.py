n, q = map(int, input().split())
a = list(map(int, input().split()))
x = list(map(int, input().split()))
for v in x:
    res = 0
    s = 0
    r = 0
    for l in range(n):
        while r < n and s + a[r] <= v:
            s += a[r]
            r += 1
        res += r - l
        if r == l:
            r += 1
        else:
            s -= a[l]
    print(res)
