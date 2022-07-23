l1, r1, l2, r2 = map(int, input().split())
l = sorted([[l1, r1], [l2, r2]])
if l[0][1] < l[1][0]:
    print(0)
elif l[0][1] < l[1][1]:
    print(l[0][1] - l[1][0])
else:
    print(l[1][1] - l[1][0])
