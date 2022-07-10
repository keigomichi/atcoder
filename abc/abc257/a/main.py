from math import ceil
n, x = map(int, input().split())
print(chr(ord('A') + ceil(x / n) - 1))
