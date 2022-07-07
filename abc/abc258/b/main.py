n = int(input())
a = [input() for _ in range(n)]
res = '0'
x = [-1, -1, -1, 0, 0, 1, 1, 1]
y = [-1, 0, 1, -1, 1, -1, 0, 1]
for i in range(n):
    for j in range(n):
        for k in range(8):
            tmp = ''
            for l in range(n):
                tmp += a[(i + x[k] * l) % n][(j + y[k] * l) % n]
                res = max(res, tmp)
print(res)
