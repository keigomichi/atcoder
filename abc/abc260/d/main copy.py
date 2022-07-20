def binary_search(key, n, s):
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
p = list(map(int, input().split()))
l = []
for v in p:
    print(l)
    i = binary_search(v, len(l), l)
    print(f'v: {v}, i: {i}')
    if i == len(l):
        l.append(v)
    else:
        l[i] = v
print(l)
