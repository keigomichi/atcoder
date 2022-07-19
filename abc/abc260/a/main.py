s = input()
res = -1
for c in s:
    if s.count(c) == 1:
        res = c
        break
print(res)
