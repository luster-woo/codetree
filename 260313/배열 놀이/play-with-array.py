n,q = map(int,input().split())
arr = list(map(int,input().split()))
for _ in range(n):
    temp = list(map(int,input().split()))
    if temp[0]==1:
        print(arr[temp[1]-1])
    elif temp[0]==2:
        if temp[1] in arr:
            idx = arr.index(temp[1])+1
            print(idx)
        else:
            print(0)
    else:
        print(*arr[temp[1]-1:temp[2]])