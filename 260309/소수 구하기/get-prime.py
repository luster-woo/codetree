n = int(input())
for x in range(1,n+1):
    cnt = 0
    for y in range(1,x):
        if x%y==0:
            cnt+=1
    if cnt==1:
        print(x,end=" ")