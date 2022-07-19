from math import gcd


def my_lcm(x, y):
    return (x * y) // gcd(x, y)


n, a, b = map(int, input().split())
na = n // a
nb = n // b
nab = n // my_lcm(a, b)
if a == b:
    print(n * (n + 1) // 2 - a * na * (na + 1) // 2)
    exit()
print(n * (n + 1) // 2 - a * na * (na + 1) // 2 - b *
      nb * (nb + 1) // 2 + my_lcm(a, b) * nab * (nab + 1) // 2)
