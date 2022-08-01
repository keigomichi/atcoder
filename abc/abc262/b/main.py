# n, m = map(int, input().split())
# l = []
# d = dict()
# for _ in range(m):
#     u, v = map(int, input().split())
#     d[(u, v)] = True
# res = 0
# for a in range(1, n - 1):
#     for b in range(a + 1, n):
#         for c in range(b + 1, n + 1):
#             if (a, b) in d and (b, c) in d and (a, c) in d:
#                 res += 1
# print(res)

n, m = map(int, input().split())
adj = [[False] * n for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    adj[u - 1][v - 1] = True
    adj[v - 1][u - 1] = True
res = 0
for a in range(n):
    for b in range(a + 1, n):
        for c in range(b + 1, n):
            if adj[a][b] and adj[b][c] and adj[a][c]:
                res += 1
print(res)
