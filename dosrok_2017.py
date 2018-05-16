n = int(input())

max = 0
max2 = 0
max13 = 0
max26 = 0
ans = 0

for i in range(n):
    k = int(input())
    if k % 26 == 0 and k > max26:
        max26 = k
    elif k % 13 == 0 and k > max13:
        max13 = k
    elif k % 2 == 0 and k > max2:
        max2 = k
    elif k > max:
        max = k
        
if max < max13:
    max = max13
    
if max < max2:
    max = max2

if max26 != 0:
    ans = max26 * max
    
else:
    ans = max13 * max2

c = int(input())
print('Вычисленное контрольное значение:', ans)

if c == ans:
    print('Контроль пройден')
    
else:
    print('Контроль не пройден')
    
    

# https://inf-ege.sdamgia.ru/problem?id=13373

    



