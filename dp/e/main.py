N, W = map(int, input().split())
w = [0] * N
v = [0] * N
for i in range(N):
    w[i], v[i] = map(int, input().split())
V = sum(v)
dp = [[10**10 for _ in range(V + 1)] for _ in range(N + 1)]
dp[0][0] = 0
for i in range(1, N + 1):
    for j in range(0, V + 1):
        if j - v[i - 1] >= 0:
            dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - v[i - 1]] + w[i - 1])
        else:
            dp[i][j] = dp[i - 1][j]
print(max([i for i in range(V + 1) if dp[N][i] <= W]))
