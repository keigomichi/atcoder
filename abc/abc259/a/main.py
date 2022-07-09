n, m, x, t, d = map(int, input().split())
print(t - d * (x - m) if m < x else t)
