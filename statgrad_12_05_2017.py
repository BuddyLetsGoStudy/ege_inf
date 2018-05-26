n = int(input())

arr = [0, 0, 0, 0, 0, 0, 0, 0]
m = 0 # частота
m_i = 0 # длина

for i in range(n):
    k = int(input())
    j = 0
    
    while k > 0:
        j += 1
        k //= 10
    
    arr[j - 1] += 1

for q in range(len(arr)):
    if arr[q] >= m:
        m = arr[q]
        m_i = q
    
print(m_i + 1, m)

