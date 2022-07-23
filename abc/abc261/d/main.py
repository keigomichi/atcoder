n, m = map(int, input().split())
x = list(map(int, input().split()))
c = [0] * m
y = [0] * m
for i in range(m):
    c[i], y[i] = map(int, input().split())
dp = [0] * (n + 1)
cnt = 0
for i in range(n):
    bns = 0
    for j in range(m):
        if c[j] == cnt + 1:
            bns = y[j]
    if dp[i] > dp[i] + x[i] + bns:
        dp[i + 1] = dp[i]
    else:
        dp[i + 1] = dp[i] + x[i] + bns
        cnt += 1
print(max(dp))
