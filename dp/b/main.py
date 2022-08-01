n, k = map(int, input().split())
h = list(map(int, input().split()))
dp = [10**10] * n
dp[0] = 0
for i in range(1, n):
    for j in range(k):
        if i - j >= 0:
            dp[i] = min(dp[i], dp[i - (j + 1)] + abs(h[i] - h[i - (j + 1)]))
print(dp[-1])
