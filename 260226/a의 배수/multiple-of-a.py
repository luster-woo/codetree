n,a = map(int,input().split())
b = 1
while b<=n:
    if b%a==0:
        print(1)
    else:
        print(0)
    b+=1