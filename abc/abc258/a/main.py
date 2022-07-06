k = int(input())
print(f'21:{k:02d}' if k < 60 else f'22:{k % 60:02d}')
