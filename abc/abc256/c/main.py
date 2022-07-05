h1, h2, h3, w1, w2, w3 = map(int, input().split())
res = 0
for a in range(1, h1):
    for b in range(1, h1):
        for d in range(1, h2):
            for e in range(1, h2):
                c = h1 - a - b
                f = h2 - d - e
                g = w1 - a - d
                h = w2 - b - e
                i = w3 - c - f
                if i != h3 - g - h:
                    continue
                if c > 0 and f > 0 and g > 0 and h > 0 and i > 0:
                    res += 1
print(res)
