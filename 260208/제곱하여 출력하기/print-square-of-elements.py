num = int(input())
arr = list(map(int,input().split()))
for i in range(num):
    arr[i]**=2
print(*arr)
