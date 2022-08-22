h, w = map(int, input().split())
g = [list(input()) for _ in range(h)]
f = [[False] * w for _ in range(h)]
i, j = 0, 0
f[0][0] = True
while True:
    if i != 0 and g[i][j] == 'U':
        i -= 1
    elif i != h - 1 and g[i][j] == 'D':
        i += 1
    elif j != 0 and g[i][j] == 'L':
        j -= 1
    elif j != w - 1 and g[i][j] == 'R':
        j += 1
    else:
        break
    if f[i][j]:
        print(-1)
        exit()
    else:
        f[i][j] = True
print(i + 1, j + 1)
