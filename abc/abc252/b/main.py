n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
max_v = max(a)
l = [i + 1 for i, x in enumerate(a) if x == max_v]
for v in l:
    if v in b:
        print('Yes')
        exit()
print('No')
