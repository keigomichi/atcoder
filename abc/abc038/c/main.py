n = int(input())
a = list(map(int, input().split()))
a.append(0)
res = 0
right = 0
for left in range(n):
    while right < n and a[right] < a[right + 1]:
        right += 1
    res += right - left + 1
    if right == left:
        right += 1
print(res)
