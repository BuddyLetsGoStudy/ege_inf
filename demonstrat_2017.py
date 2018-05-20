n = int(input())
sum = 0

for i in range(n):
    a, b = map(int, input().split())
    sum += max(a, b)
    
# https://inf-ege.sdamgia.ru/problem?id=11363
