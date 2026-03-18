n,k = map(int,input().split())
arr = [[0]*n for _ in range(n)]
for _ in range(k):
    a,b = map(int,input().split())
    arr[a-1][b-1]=a*b
for x in range(n):
    for y in range(n):
        print(arr[x][y],end=" ")
    print()