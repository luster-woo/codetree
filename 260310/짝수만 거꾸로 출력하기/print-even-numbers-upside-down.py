n = int(input())
arr = list(map(int,input().split()))
temp = []
for x in arr[::-1]:
    if x%2==0:
        temp.append(x)
print(*temp)