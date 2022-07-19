# アルゴリズム

## 二分探索

```python
# https://qiita.com/drken/items/97e37dd6143e33a64c8c
def binary_search(key, n, s):
    left = -1
    right = n
    while right - left > 1:
        mid = (left + right) // 2
        if s[mid] >= key:
            right = mid
        else:
            left = mid
    return right
```

## Union-Find 木

```python
# https://note.nkmk.me/python-union-find/
from collections import defaultdict


class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())
```

## 多重集合

```python
# https://qiita.com/mymelochan/items/0c72d8b7ae8d9c3d836a
from heapq import heappop, heappush
from collections import defaultdict


class MultiSet:
    def __init__(self, deleteFlag=True):
        self.len = 0
        self.f = defaultdict(int)
        self.pos = []
        self.neg = []
        self.deleteFlag = deleteFlag

    def _delete(self, key):
        if self.deleteFlag and self.f[key] == 0:
            del self.f[key]

    def add(self, x, key=None):
        if key is None:
            key = x
        self.len += 1
        heappush(self.pos, (x, key))
        heappush(self.neg, (-x, key))
        self.f[key] += 1

    def searchMax(self, returnKey=False):
        while True:
            x, key = self.neg[0]
            if self.f[key]:
                if returnKey:
                    return -x, key
                else:
                    return -x
            else:
                heappop(self.neg)

    def searchMin(self, returnKey=False):
        while True:
            x, key = self.pos[0]
            if self.f[key]:
                if returnKey:
                    return x, key
                else:
                    return x
            else:
                heappop(self.pos)

    def deleteKey(self, key):
        self.f[key] -= 1
        self._delete(key)
        self.len -= 1

    def exist(self, key):
        if self.f.get(key) is None:
            return False
        else:
            return True
```

## 最小公倍数

https://note.nkmk.me/python-gcd-lcm/

```python
def lcm(x, y):
    return (x * y) // gcd(x, y)
```

## 等差数列の和

```python
def sum_ap(n, a, d):
    return n * (2 * a + (n - 1) * d) // 2
```
