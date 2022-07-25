def binary_search(key, n, a):
    left = -1
    right = n
    while right - left > 1:
        mid = (left + right) // 2
        if a[mid] >= key:
            right = mid
        else:
            left = mid
    return right


n, q = map(int, input().split())
a = sorted(list(map(int, input().split())))
s = [0] * (n + 1)
for i in range(n):
    s[i + 1] = s[i] + a[i]
for _ in range(q):
    x = int(input())
    k = binary_search(x, n, a)
    print(k * x - s[k] + s[n] - s[k] - (n - k) * x)
