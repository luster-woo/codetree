a,b = map(int,input().split())
if a%2==1:
    for x in range(a,b-1,-2):
        print(x,end=" ")
else:
    for x in range(a-1,b-1,-2):
        print(x,end=" ")