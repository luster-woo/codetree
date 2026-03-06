n  = int(input())
cnt = 1
for x in range(n):
    for y in range(n):
        print(cnt,end=" ")
        if (x%2==0 and y<n-1) or (x%2==1 and y==n-1):
            cnt+=1
        else:
            cnt+=2
    print()