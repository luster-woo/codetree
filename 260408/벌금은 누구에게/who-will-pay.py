n,m,k = map(int,input().split())
arr = [0]*n
for x in range(m):
    temp = int(input())
    arr[temp-1]+=1
    if arr[temp-1]>=k:
        print(x+1)
        exit()

print(-1)