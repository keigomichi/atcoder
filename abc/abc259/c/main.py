s = input()
t = input()
ls = []
lt = []
cnt = 1
for i in range(1, len(s)):
    if i == len(s) - 1:  # 番兵を利用可
        if s[i - 1] != s[i]:
            ls.append([s[i - 1], cnt])
            ls.append([s[i], 1])
        else:
            ls.append([s[i], cnt + 1])
        break
    if s[i - 1] != s[i]:
        ls.append([s[i - 1], cnt])
        cnt = 1
    if s[i - 1] == s[i]:
        cnt += 1
cnt = 1
for i in range(1, len(t)):
    if i == len(t) - 1:
        if t[i - 1] != t[i]:
            lt.append([t[i - 1], cnt])
            lt.append([t[i], 1])
        else:
            lt.append([t[i], cnt + 1])
        break
    if t[i - 1] != t[i]:
        lt.append([t[i - 1], cnt])
        cnt = 1
    if t[i - 1] == t[i]:
        cnt += 1
if len(ls) != len(lt):
    print('No')
    exit()
for m, n in zip(ls, lt):
    if (m[0] != n[0]) or (m[1] == 1 and n[1] > 1) or (m[1] >= 2 and n[1] < m[1]):
        print('No')
        break  # exit()
else:
    print('Yes')
