n = int(input())
for x in range(1,n+1):
    for y in range(1,n+1):
        if (x+y)%4==0:
            print((x,y),end=" ")
            print()
        else:
            print((x,y),end=" ")