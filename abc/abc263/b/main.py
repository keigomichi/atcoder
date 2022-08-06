n = int(input())
p = list(map(int, input().split()))
v = p[-1]
res = 0
while v >= 2 and p[v - 2] >= 1:
    v = p[v - 2]
    res += 1
print(res + 1)
