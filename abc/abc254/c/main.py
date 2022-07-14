n, k = map(int, input().split())
a = list(map(int, input().split()))
b = [sorted(a[i::k]) for i in range(k)]
c = [b[i % k][i // k] for i in range(n)]
print('Yes' if c == sorted(a) else 'No')
