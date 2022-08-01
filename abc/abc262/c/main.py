# n = int(input())
# a = list(map(int, input().split()))
# d = dict()
# for i in range(n):
#     d[i + 1] = a[i]
# res = 0
# cnt = 0
# for i in range(1, n + 1):
#     j = d[i]
#     if d[j] == i:
#         res += 1
#     if i == j:
#         res -= 1
#         cnt += 1
# res //= 2
# if cnt > 1:
#     res += cnt * (cnt - 1) // 2
# print(res)

n = int(input())
a = list(map(int, input().split()))
res = 0
same = 0
for i in range(n):
    if a[i] == i + 1:
        same += 1
        continue
    if a[a[i] - 1] == i + 1:
        res += 1
print(res // 2 + same * (same - 1) // 2)
