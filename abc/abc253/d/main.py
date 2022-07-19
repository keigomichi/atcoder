from math import gcd


def lcm(x, y):
    return (x * y) // gcd(x, y)


def sum_ap(n, a, d):
    return n * (2 * a + (n - 1) * d) // 2


n, a, b = map(int, input().split())
na = n // a
nb = n // b
nab = n // lcm(a, b)
print(sum_ap(n, 1, 1) - sum_ap(na, a, a) - sum_ap(nb, b, b) + sum_ap(nab, lcm(a, b), lcm(a, b)))
