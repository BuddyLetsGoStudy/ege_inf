n = int(input())
arr = []
counter = 0

for i in range(5):
    arr.append(int(input()))
    
for i in range(4):
    for k in range(i + 1, 5):
        if (arr[i] + arr[k]) % 2 != 0 and arr[i] % 13 == 0:
            counter += 1
            
for i in range(n - 5):
    x = int(input())
    arr.pop(0)
    arr.append(x)
    for k in range(4):
        if (arr[4] + arr[k]) % 2 != 0 and arr[4] * arr[k] % 13 == 0:
            counter += 1
            
print(counter)
                

