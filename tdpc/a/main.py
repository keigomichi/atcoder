n = int(input())
p = list(map(int, input().split()))
P = sum(p)
dp = [[False for _ in range(P + 1)] for _ in range(n + 1)]
dp[0][0] = True
for i in range(1, n + 1):
    for j in range(P + 1):
        dp[i][j] = dp[i - 1][j] or (j - p[i - 1] >=
                                    0 and dp[i - 1][j - p[i - 1]])
print(dp[n].count(True))
