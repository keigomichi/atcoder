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
