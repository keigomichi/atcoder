from math import sqrt
print('Yes' if sqrt(float(''.join(list(input().split())))).is_integer() else 'No')
