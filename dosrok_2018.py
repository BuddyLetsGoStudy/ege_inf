n = int(input())
sumall = (n * (n - 1)) // 2

d2 = 0
d17 = 0
d34 = 0

for i in range(n):
    k = int(input())
    if k % 34 == 0:
        d34 += 1
    elif k % 17 == 0:
        d17 += 1
    elif k % 2 == 0:
        d2 += 1

print(sumall - ((d34 * (d34 - 1)) // 2 + d34 * (n - d34) + d2 * d17))

# https://inf-ege.sdamgia.ru/problem?id=15643

