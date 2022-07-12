n, k = map(int, input().split())
s = [int(input()) for _ in range(n)]
if 0 in s:
    print(n)
    exit()
res = 0
pro = 1
right = 0
for left in range(n):
    while right < n and pro * s[right] <= k:
        pro *= s[right]
        right += 1
    res = max(right - left, res)
    if right == left:
        right += 1
    else:
        pro /= s[left]
print(res)
