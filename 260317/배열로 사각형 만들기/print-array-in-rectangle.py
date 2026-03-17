arr = [[0]*5 for _ in range(5)]
for x in range(5):
    for y in range(5):
        if x==0 or y==0:
            arr[x][y]=1
        else:
            arr[x][y]=arr[x-1][y]+arr[x][y-1]
for x in range(5):
    for y in range(5):
        print(arr[x][y],end=" ")
    print()