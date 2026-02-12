n, m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
arr_1 = [list(map(int,input().split())) for _ in range(n)]
for i in range(n):
    for j in range(m):
        if arr[i][j] !=arr_1[i][j]:
            print(1,end=" ")
        else:
            print(0,end=" ")
        