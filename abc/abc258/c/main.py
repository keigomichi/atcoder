n, q = map(int, input().split())
s = input()
top = 0
for _ in range(q):
    t, x = map(int, input().split())
    if t == 1:
        top = (top - x) % n
    elif t == 2:
        print(s[(top + x - 1) % n])
