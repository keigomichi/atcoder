n, k, q = map(int, input().split())
a = list(map(int, input().split()))
l = list(map(int, input().split()))
# for i in range(k):
#     a[i] -= 1
# for i in range(q):
#     l[i] -= 1
# for v in l:
#     if (a[v] < n - 1) and (a[v] + 1 not in a):
#         a[v] += 1
# for i in range(k):
#     a[i] += 1
# print(*a)
a.append(n + 1)
for v in l:
    v -= 1
    if a[v] + 1 != a[v + 1]:
        a[v] += 1
print(*a[:-1])
