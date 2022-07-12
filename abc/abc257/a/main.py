# from math import ceil
# n, x = map(int, input().split())
# print(chr(ord('A') + ceil(x / n) - 1))
n, x = map(int, input().split())
s = []
for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
    for _ in range(n):
        s.append(c)
print(s[x - 1])
