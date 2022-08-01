# y = int(input())
# if y % 4 == 0:
#     print(y + 2)
# elif y % 4 == 2:
#     print(y)
# else:
#     print(y + y % 4)

y = int(input())
while y % 4 != 2:
    y += 1
print(y)