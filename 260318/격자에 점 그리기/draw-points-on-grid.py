n,k = map(int,input().split())
arr = [[0]*n for _ in range(n)]
for c in range(1,k+1):
    a,b = map(int,input().split())
    arr[a-1][b-1]=c
for x in range(n):
    for y in range(n):
        print(arr[x][y],end=" ")
    print()