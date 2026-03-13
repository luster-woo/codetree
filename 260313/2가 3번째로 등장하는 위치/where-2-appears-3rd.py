n = int(input())
cnt = 0
i= 0
arr= list(map(int,input().split()))
for x in arr:
    if x==2:
        cnt+=1
    if cnt==3:
        print(i+1)
        break
    i+=1