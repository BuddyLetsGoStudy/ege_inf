n = int(input())

arr = [0, 0, 0, 0, 0, 0, 0]

for i in range(n):
    k = int(input())
    arr[k % 7] += 1
    
r7 = arr[0] * (arr[0] - 1) // 2
print(arr[1] * arr[6] + arr[2] * arr[5] + arr[3] * arr[4] + r7)

# https://inf-ege.sdamgia.ru/problem?id=14713
