n = int(input())
arr = [[0]*n for _ in range(n)]
cnt =1
for x in range(n-1,-1,-1):
    for y in range(n-1,-1,-1):
        if y%2==1:
            arr[y][x]=cnt
            cnt+=1
        else:
            arr[n-y+1][x]=cnt
            cnt+=1
for x in arr:
    print(*x)