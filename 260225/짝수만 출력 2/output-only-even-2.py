a,b = map(int,input().split())
if a%2==0:
    while a>=b:
        print(a,end=" ")
        a-=2
else:
    a-=1
    while a>=b:
        print(a,end=" ")
        a-=2