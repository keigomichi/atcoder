from math import sin, cos, radians
a, b, d = map(int, input().split())
sind = sin(radians(d))
cosd = cos(radians(d))
print(a * cosd - b * sind, a * sind + b * cosd)
