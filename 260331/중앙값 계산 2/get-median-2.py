n = int(input())
arr = list(map(int, input().split()))
for x in range(0,n,2):
    temp = arr[:x+1]
    temp.sort()
    print(temp[(x+1)//2],end=" ")