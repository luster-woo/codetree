n  = int(input())
temp = list(map(int,input().split()))
result = []
for x in temp:
    if x%2==0:
        result.append(x)
print(*result)