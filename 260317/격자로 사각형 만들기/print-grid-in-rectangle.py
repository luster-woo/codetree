n = int(input())
arr = [[0]*n for _ in range(n)]
for x in range(n):
    for y in range(n):
        if y==0 or x ==0:
            arr[x][y]=1
        else:
            arr[x][y]=arr[x-1][y-1]+arr[x-1][y]+arr[x][y-1]
for x in range(n):
    for y in range(n):
        print(arr[x][y],end=" ")
    print()