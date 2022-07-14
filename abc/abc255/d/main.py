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
s = [0] * n
s[0] = a[0]
for i in range(1, n):
    s[i] = s[i - 1] + a[i]
for _ in range(q):
    x = int(input())
    k = binary_search(x, n, a)
    print(abs(s[k - 1] - k * x) + abs(s[n - 1] - s[k - 1] - (n - k) * x))
