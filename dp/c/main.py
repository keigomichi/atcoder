n = int(input())
l = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1 for _ in range(3)] for _ in range(n)]
for i in range(3):
    dp[0][i] = l[0][i]
for i in range(1, n):
    for j in range(3):
        dp[i][j] = max(dp[i - 1][(j + 1) % 3] + l[i][j],
                       dp[i - 1][(j + 2) % 3] + l[i][j])
print(max(dp[-1]))
