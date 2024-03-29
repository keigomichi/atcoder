"""
【特集】典型的な動的計画法のパターンを整理 ～ナップサック DP 編～
"""
"""
問題1: 最大和問題
"""
# n = int(input())
# a = list(map(int, input().split()))
# dp = [-10**10] * (n + 1)
# dp[0] = 0
# for i in range(1, n + 1):
#     dp[i] = max(dp[i - 1], dp[i - 1] + a[i - 1])
# print(dp[-1])

"""
問題2: ナップザック問題
"""
# n, w = map(int, input().split())
# x = [0] * n
# y = [0] * n
# for i in range(n):
#     x[i], y[i] = map(int, input().split())
# dp = [[0 for _ in range(w + 1)] for _ in range(n + 1)]
# for i in range(1, n + 1):
#     for j in range(1, w + 1):
#         if j >= x[i - 1]:
#             dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - x[i - 1]] + y[i - 1])
#         else:
#             dp[i][j] = dp[i - 1][j]
# print(dp)
# print(dp[-1][-1])

"""
問題3: 部分和問題
"""
# n, m = map(int, input().split())
# a = list(map(int, input().split()))
# dp = [[False for _ in range(m + 1)] for _ in range(n + 1)]
# dp[0][0] = True
# for i in range(1, n + 1):
#     for j in range(m + 1):
#         dp[i][j] = dp[i - 1][j] or (j - a[i - 1] >=
#                                     0 and dp[i - 1][j - a[i - 1]])
# print('Yes' if dp[n][m] else 'No')

"""
問題4: 部分和数え上げ問題
"""
# n, m = map(int, input().split())
# a = list(map(int, input().split()))
# dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
# dp[0][0] = 1
# for i in range(1, n + 1):
#     for j in range(m + 1):
#         dp[i][j] += dp[i - 1][j]
#         if j - a[i - 1] >= 0:
#             dp[i][j] += dp[i - 1][j - a[i - 1]]
# print(dp[n][m] % 1000)

"""
問題5: 最小個数部分和問題
"""
# n, m = map(int, input().split())
# a = list(map(int, input().split()))
# dp = [[10**10 for _ in range(m + 1)] for _ in range(n + 1)]
# dp[0][0] = 0
# for i in range(1, n + 1):
#     for j in range(m + 1):
#         dp[i][j] = min(dp[i][j], dp[i - 1][j])
#         if j - a[i - 1] >= 0:
#             dp[i][j] = min(dp[i][j], dp[i - 1][j - a[i - 1]] + 1)
# print(dp[n][m] if dp[n][m] < 10**10 else -1)

"""
問題6: K個以内部分和問題
"""
# n, m, k = map(int, input().split())
# a = list(map(int, input().split()))
# dp = [[10**10 for _ in range(m + 1)] for _ in range(n + 1)]
# dp[0][0] = 0
# for i in range(1, n + 1):
#     for j in range(m + 1):
#         dp[i][j] = min(dp[i][j], dp[i - 1][j])
#         if j - a[i - 1] >= 0:
#             dp[i][j] = min(dp[i][j], dp[i - 1][j - a[i - 1]] + 1)
# print('Yes' if dp[n][m] <= k else 'No')

"""
問題7: 個数制限付き部分和問題
"""
"""
問題8: 最長共通部分列(LCS)問題
"""
s = input()
t = input()
len_s = len(s)
len_t = len(t)
dp = [[0 for _ in range(len_t + 1)] for _ in range(len_s + 1)]
for i in range(1, len_s + 1):
    for j in range(1, len_t + 1):
        if s[i - 1] == t[j - 1]:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1] + 1)
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
print(dp[len_s][len_t])

"""
問題9: 最小コスト弾性マッチング問題
"""
"""
問題10: レーベンシュタイン距離(diffコマンド)
"""
"""
問題11: 発電計画問題
"""
