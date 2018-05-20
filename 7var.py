n = int(input())

d_max = 0
d_min = 100001

for i in range(n):
    k1, k2 = map(int, input().split())
    k1 **= 2
    k2 **= 2
    
    if k1 >= k2:
        d_max += k1
        if k1 - k2 < d_min and k1 - k2 != 0 and (k1 - k2) % 2 != 0:
            d_min = k1 - k2
    else:
        d_max += k2
        if k2 - k1 < d_min and k2 - k1 != 0 and (k2 - k1) % 2 != 0:
            d_min = k2 - k1
            
if d_max % 2 != 0:
    print(d_max)
elif d_min != 100001:
    print(d_max - d_min)
else:
    print(0)

