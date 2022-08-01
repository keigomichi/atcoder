n = int(input())
dp = [i for i in range(n + 1)]
for i in range(2, n + 1):
    j = 1
    while i - 6**j >= 0:
        dp[i] = min(dp[i], dp[i - 6**j] + 1)
        j += 1
    k = 1
    while i - 9**k >= 0:
        dp[i] = min(dp[i], dp[i - 9**k] + 1)
        k += 1
print(dp[-1])
