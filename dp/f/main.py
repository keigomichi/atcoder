s = input()
t = input()
len_s = len(s)
len_t = len(t)
dp = [[0 for _ in range(len_t + 1)] for _ in range(len_s + 1)]
for i in range(1, len_s + 1):
    for j in range(1, len_t + 1):
        if s[i - 1] == t[j - 1]:
            dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + 1)
        dp[i][j] = max(dp[i][j], dp[i - 1][j])
        dp[i][j] = max(dp[i][j], dp[i][j - 1])
res = ""
i = len_s
j = len_t
while i > 0 and j > 0:
    if dp[i][j] == dp[i - 1][j]:
        i -= 1
    elif dp[i][j] == dp[i][j - 1]:
        j -= 1
    else:
        res += s[i - 1]
        i -= 1
        j -= 1
print(res[::-1])
