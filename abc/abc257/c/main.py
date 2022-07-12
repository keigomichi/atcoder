n = int(input())
s = list(map(int, input()))
w = list(map(int, input().split()))
l = []
for a, b in zip(s, w):
    l.append([b, a])
# cnt_child = 0
# cnt_adult = sum(s)
# res = cnt_child + cnt_adult
cnt = sum(s)
res = cnt
l.sort()
l.append([0, 0])
for i in range(n):
    if l[i][1] == 0:
        # cnt_child += 1
        cnt += 1
    else:
        # cnt_adult -= 1
        cnt -= 1
    if l[i][0] != l[i + 1][0]:
        # res = max(res, cnt_child + cnt_adult)
        res = max(res, cnt)
print(res)
