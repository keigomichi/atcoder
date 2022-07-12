from statistics import median
a, b, c = map(int, input().split())
print('Yes' if b == median([a, b, c]) else 'No')
