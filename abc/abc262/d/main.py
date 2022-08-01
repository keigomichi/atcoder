n = int(input())
a = list(map(int, input().split()))
res = 0
for i in range(n + 1):
    dp = [[[0] * (n + 1) for _ in range(n + 1)] for _ in range(n + 1)]
    dp[0][0][0] = 1
    for j in range(n):
        for k in range(i + 1):
            for l in range(i):
                dp[j + 1][k][l] += dp[j][k][l]
                if k != i:
                    dp[j + 1][k + 1][(l + a[j]) % i] += dp[j][k][l]
    res += dp[n][i][0]
print(res % 998244353)
