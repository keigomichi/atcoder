from math import factorial
n = int(input())
a = list(map(int, input().split()))
s = set(a)
d = dict()
for e in s:
    d[e] = 0
for v in a:
    d[v] += 1
print(d)
m = len(s)
res = factorial(m) // (factorial(m - 3) * factorial(3))
for v in d.values():
    res *= v
print(res)
