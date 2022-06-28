n = int(input())
a = list(map(int, input().split()))
print(sum([1 for i in range(n) if sum(a[i:n]) > 3]))
