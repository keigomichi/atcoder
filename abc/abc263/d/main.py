n, l, r = map(int, input().split())
a = list(map(int, input().split()))
sl = [0] * n
sr = [0] * n

for i in range(n):
    if i == 0:
        sl[i] = l - a[i]
        sr[i] = r - a[n - 1 - i]
    else:
        sl[i] = sl[i - 1] + (l - a[i])
        sr[i] = sr[i - 1] + (r - a[n - 1 - i])
res = 10**20
for i in range(n):
    print(sl[i], min(sr[:-(i + 1)]))