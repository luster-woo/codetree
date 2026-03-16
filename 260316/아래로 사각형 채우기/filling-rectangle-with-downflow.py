cnt = 1
n = int(input())
arr = [[0]*n for _ in range(n)]
for x in range(n):
    for y in range(n):
        arr[y][x]=cnt
        cnt+=1
for x in range(n):
    for y in range(n):
        print(arr[x][y],end=" ")
    print()
