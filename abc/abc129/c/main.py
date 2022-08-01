n, m = map(int, input().split())
b = [True] * (n + 1)
for _ in range(m):
    b[int(input())] = False
dp = [0] * (n + 1)
dp[0] = 1
dp[1] = 1
for i in range(2, n + 1):
    for j in range(1, 3):
        if b[i - j]:
            dp[i] += dp[i - j]
print(dp[n] % 1000000007)
