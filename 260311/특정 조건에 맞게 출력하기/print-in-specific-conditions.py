arr = list(map(int,input().split()))
idx = arr.index(0)
temp = []
for x in arr[:idx]:
    if x%2==1:
        temp.append(x+3)
    else:
        temp.append(x//2)
print(*temp) 