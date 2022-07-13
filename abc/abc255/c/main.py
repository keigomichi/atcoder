def getDistance(x, y):
    if x > y:
        return x - y
    else:
        return y - x


x, a, d, n = map(int, input().split())
left = -1
right = n
if d < 0:
    while right - left > 1:
        mid = (left + right) // 2
        if a + mid * d >= x:
            left = mid
        else:
            right = mid
else:
    while right - left > 1:
        mid = (left + right) // 2
        if a + mid * d >= x:
            right = mid
        else:
            left = mid
res1 = getDistance(a + right * d, x)
res2 = getDistance(a + (right - 1) * d, x)
if right == 0:
    print(res1)
    exit()
if right == n:
    print(res2)
    exit()
print(min(res1, res2))
