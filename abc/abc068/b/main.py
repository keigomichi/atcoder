# n = int(input())
# res = -1
# ans = -1
# for i in range(1, n + 1):
#     cnt = 0
#     tmp = i
#     while (i % 2 == 0):
#         i //= 2
#         cnt += 1
#     if res < cnt:
#         res = cnt
#         ans = tmp
# print(ans)

from math import log2, floor
print(2**floor(log2(int(input()))))
