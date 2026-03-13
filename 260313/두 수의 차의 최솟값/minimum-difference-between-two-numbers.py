import math
n = int(input())
arr = list(map(int,input().split()))
min_val = 10**9
for x in range(n):
    for y in range(x,n):
        if abs(arr[y]-arr[x])<min_val:
            min_val = abs(arr[y]-arr[x])
print(min_val)