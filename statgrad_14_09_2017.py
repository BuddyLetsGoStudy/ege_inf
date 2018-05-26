n = int(input())
m = 0
ans = 0

arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(n):
    k = int(input())
    k1 = k % 10
    k10 = k % 100 // 10
    
    arr[k1 + k10] += 1

for j in range(len(arr)):
    if arr[j] >= m:
       m = arr[j]
       ans = j
        
print(ans)


