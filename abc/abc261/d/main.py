n, m = map(int, input().split())
x = [0] + list(map(int, input().split()))
y = [0] * (n + 1)
for _ in range(m):
    c, v = map(int, input().split())
    y[c] = v
dp = [[-10000000000] * (n + 1) for _ in range(n + 1)]
dp[0][0] = 0
for i in range(1, n + 1):
    for j in range(i + 1):
        if j == 0:
            dp[i][0] = dp[i - 1][0]
        else:
            dp[i][j] = dp[i - 1][j - 1] + x[i] + y[j]
            dp[i][0] = max(dp[i][0], dp[i - 1][j])
print(max(dp[n]))
