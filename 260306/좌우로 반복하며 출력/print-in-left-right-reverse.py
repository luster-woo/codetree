n = int(input())
for x in range(1,n+1):
    for y in range(1,n+1):
        if x%2==1:
            print(y,end="")
        else:
            print(n-y+1,end="")
    print()