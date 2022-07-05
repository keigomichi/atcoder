n = int(input())
l = []
highest = [0, 0] # [pt, th]
for i in range(n):
    s, t = input().split()
    t = int(t)
    if not (s in l):
        l.append(s)
        if highest[0] < t:
            highest[0] = t
            highest[1] = i
print(highest[1] + 1)
n = int(input())
dic = dict()
highest = [0, 0] # [pt, th]
for i in range(n):
    s, t = input().split()
    t = int(t)
    if s not in dic:
        dic[s] = True
        if highest[0] < t:
            highest[0] = t
            highest[1] = i
print(highest[1] + 1)
