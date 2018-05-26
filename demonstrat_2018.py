n = int(input())

d26 = 0
d13 = 0
d2 = 0

for i in range(n):
    k = int(input())
    if k % 26 == 0:
        d26 += 1
    elif k % 13 == 0:
        d13 += 1
    elif k % 2 == 0:
        d2 += 1
        
print((d26 * (d26 - 1)) // 2 + d26 * (n - d26) + d2 * d13)

