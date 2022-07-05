n = int(input())
t = [0] * n
x = [0] * n
y = [0] * n
for i in range(n):
    t[i], x[i], y[i] = map(int, input().split())
    if i == 0:
        dt = t[i]
        dist = x[i] + y[i]
    else:
        dt = t[i] - t[i - 1]
        dist = abs(x[i] - x[i - 1]) + abs(y[i] - y[i - 1])
    if dt < dist or dt % 2 != dist % 2:
        print('No')
        exit()
print('Yes')
