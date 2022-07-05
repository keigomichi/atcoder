def binary_search(key):
    left = -1
    right = n
    while right - left > 1:
        mid = (left + right) // 2
        if s[mid] >= key:
            right = mid
        else:
            left = mid
    return right


n, k = map(int, input().split())
a = list(map(int, input().split()))
s = a
for i in range(1, n):
    s[i] += s[i - 1]
res = n - binary_search(k)
for v in s:
    res += n - binary_search(k + v)
print(res)
