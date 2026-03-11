arr = list(map(int,input().split()))
idx = 0
for x in range(10):
    if arr[x]%3==0:
        idx = x-1
        break

print(arr[idx])