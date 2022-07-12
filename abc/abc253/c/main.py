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

    def popMax(self, returnKey=False):
        while True:
            x, key = heappop(self.neg)
            if self.f[key]:
                self.f[key] -= 1
                self.len -= 1
                self._delete(key)
                if returnKey:
                    return -x, key
                else:
                    return x

    def popMin(self, returnKey=False):
        while True:
            x, key = heappop(self.pos)
            if self.f[key]:
                self.f[key] -= 1
                self.len -= 1
                self._delete(key)
                if returnKey:
                    return x, key
                else:
                    return x

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


q = int(input())
s = MultiSet()
for _ in range(q):
    l = list(map(int, input().split()))
    if l[0] == 1:
        s.add(l[1])
    elif l[0] == 2:
        while l[2] and s.exist(l[1]):
            s.deleteKey(l[1])
            l[2] -= 1
    elif l[0] == 3:
        print(s.searchMax() - s.searchMin())
