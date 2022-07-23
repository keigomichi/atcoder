n = int(input())
d = dict()
for _ in range(n):
    s = input()
    if s not in d:
        d[s] = 0
        print(s)
    else:
        d[s] += 1
        print(f'{s}({d[s]})')
