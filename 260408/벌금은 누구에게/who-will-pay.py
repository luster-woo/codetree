n,m,k = map(int,input().split())
arr = [0]*n
for x in range(n):
    temp = int(input())
    if temp>=k:
        print(x+1)
        exit()