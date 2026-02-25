a,b = map(str,input().split())
if a=="A":
    for x in range(1,int(b)+1):
        print(x,end=" ")
else:
    for x in range(int(b),0,-1):
        print(x,end=" ")