n = int(input())
a = [list(map(int, input())) for _ in range(n)]
res = 0
for i in range(n):
    for j in range(n):
        # 上
        tmp = 0
        x, y = i, j
        for k in range(n):
            tmp += a[x][y] * (10 ** (n - k - 1))
            x -= 1
            if x < 0:
                x += n
        res = max(res, tmp)
        # 下
        tmp = 0
        x, y = i, j
        for k in range(n):
            tmp += a[x][y] * (10 ** (n - k - 1))
            x += 1
            if x > n - 1:
                x -= n
        res = max(res, tmp)
        # 左
        tmp = 0
        x, y = i, j
        for k in range(n):
            tmp += a[x][y] * (10 ** (n - k - 1))
            y -= 1
            if y < 0:
                y += n
        res = max(res, tmp)
        # 右
        tmp = 0
        x, y = i, j
        for k in range(n):
            tmp += a[x][y] * (10 ** (n - k - 1))
            y += 1
            if y > n - 1:
                y -= n
        res = max(res, tmp)
        # 斜め(左下方向)
        tmp = 0
        x, y = i, j
        for k in range(n):
            tmp += a[x][y] * (10 ** (n - k - 1))
            x -= 1
            y -= 1
            if x < 0:
                x += n
            if y < 0:
                y += n
        res = max(res, tmp)
        # 斜め(右下方向)
        tmp = 0
        x, y = i, j
        for k in range(n):
            tmp += a[x][y] * (10 ** (n - k - 1))
            x += 1
            y += 1
            if x > n - 1:
                x -= n
            if y > n - 1:
                y -= n
        res = max(res, tmp)
        # 斜め(右上方向)
        tmp = 0
        x, y = i, j
        for k in range(n):
            tmp += a[x][y] * (10 ** (n - k - 1))
            x -= 1
            y += 1
            if x < 0:
                x += n
            if y > n - 1:
                y -= n
        res = max(res, tmp)
        # 斜め(左下方向)
        tmp = 0
        x, y = i, j
        for k in range(n):
            tmp += a[x][y] * (10 ** (n - k - 1))
            x += 1
            y -= 1
            if x > n - 1:
                x -= n
            if y < 0:
                y += n
        res = max(res, tmp)
print(res)
