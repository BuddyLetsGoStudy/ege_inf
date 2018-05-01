n = int(input())
arr = []
ans = 0

for i in range(n):
    t = int(input())
    arr.append(t)

for j in range(n):
    for q in range(1, len(arr)):
        if arr[0] * arr[q] % 58 == 0:
            ans += 1
    arr = arr[1::]

print(ans)

