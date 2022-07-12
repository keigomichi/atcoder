h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]
res = []
for i in range(h):
    for j in range(w):
        if s[i][j] == 'o':
            res.append([i, j])
print(abs(res[0][0] - res[1][0]) + abs(res[0][1] - res[1][1]))
