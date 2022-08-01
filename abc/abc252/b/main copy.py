n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
max_v = max(a)
l = [i for i, x in enumerate(a) if x == max_v]
for v in b:
    if v - 1 in l:
        print('Yes')
        exit()
print('No')
