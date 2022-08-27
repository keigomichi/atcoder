n = int(input())
t = [0] * n
x = [0] * n
a = [0] * n
for i in range(n):
    t[i], x[i], a[i] = map(int, input().split())
t_max = max(t)
l = [[0] * 5 for _ in range(t_max + 1)]
for i in range(n):
    l[t[i]][x[i]] = a[i]
dp = [[-10**10]*5 for _ in range(t_max + 1)]
dp[0][0] = 0
for i in range(1, t_max + 1):
    for j in range(5):
        dp[i][j] = max(dp[i][j], dp[i - 1][j] + l[i][j])
        if j > 0:
            dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + l[i][j])
print(max(list(map(lambda x: max(x), dp))))
