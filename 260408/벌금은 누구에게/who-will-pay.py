n,m,k = map(int,input().split())
arr = [0]*n
for x in range(m):
    temp = int(input())
    arr[temp-1]+=1
for x in range(n):
    if arr[x]>=k:
        print(x+1)
        exit()
print(-1)