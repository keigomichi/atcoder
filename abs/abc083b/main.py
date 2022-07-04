n, a, b = map(int, input().split())
res = 0
for i in range(1, n + 1):
    sum = 0
    tmp = i
    while i > 0:
        sum += i % 10
        i //= 10
    if a <= sum <= b:
        res += tmp
print(res)
