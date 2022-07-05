s = input()
d = {
    'dream': 5,
    'dreamer': 7,
    'erase': 5,
    'eraser': 6
}
i = 0
l = len(s)
while i < l:
    for key, value in d.items():
        if s[:-i].endswith(key) or (i == 0 and s[:].endswith(key)):
            i += value
            break
    else:
        print('NO')
        exit()
print('YES')
