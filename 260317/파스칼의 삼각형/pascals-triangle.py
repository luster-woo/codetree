n = int(input())
arr = [[0]*n for _ in range(n)]
for x in range(n):
    for y in range(n):
        if y==0:
            arr[x][y]=1
        elif x==y:
            arr[x][y]=1
        else:
            arr[x][y]=arr[x-1][y-1]+arr[x-1][y]
for x in range(n):
    for y in range(n):
        if arr[x][y]!=0:
            print(arr[x][y],end=" ")
    print()