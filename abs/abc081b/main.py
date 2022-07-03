n = int(input())
a = list(map(int, input().split()))
res = 1000000000
for v in a:
    cnt = 0
    while(v % 2 == 0):
        v //= 2
        cnt += 1
        if v % 2 == 1:
            break
    res = min(res, cnt)
print(res)