arr = list(map(int,input().split()))

if 0 in arr:
    arr = arr[:arr.index(0)]

print(*arr[::-1])