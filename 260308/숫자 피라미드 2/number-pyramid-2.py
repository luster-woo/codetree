cnt=1
n= int(input())
for x in range(1,n+1):
    for y in range(1,x+1):
        print(cnt,end=" ")
        cnt+=1
    print()