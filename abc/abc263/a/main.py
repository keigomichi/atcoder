a, b, c, d, e = map(int, input().split())
x = [a]
y = []
flag = True
for v in [b, c, d, e]:
    if a == v:
        x.append(v)
    elif flag:
        y.append(v)
        flag = False
    elif y[0] == v:
        y.append(v)
if len(x) == 3 and len(y) == 2 or len(x) == 2 and len(y) == 3:
    print('Yes')
else:
    print('No')
