n = int(input())

min_ = 1001
min2 = 1001
min3 = 1001
min6 = 1001

ans = 0

for i in range(n):
    k = int(input())
    if k % 6 == 0 and k < min6:
        min6 = k
    elif k % 3  == 0 and k < min3:
        min3 = k
    elif k % 2 == 0 and k < min2:
        min2 = k 
    elif k < min_:
        min_ = k
        

if min2 < min_:
    min_ = min2
    
if min3 < min_:
    min_ = min3
    
if min6 * min_ < min3 * min2:
    ans = min6 * min_
else:
    ans = min2 * min3
    
check = int(input())

print('Вычисленное контрольное значение:', ans)

if check == ans:
    print('Контроль пройден')
else:
    print('Контроль не пройден')    


# https://inf-ege.sdamgia.ru/problem?id=11128
