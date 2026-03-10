arr = list(map(int,input().split()))

if 0 in arr:
    arr = arr[:arr.index(0)]

print(f'{sum(arr)} {sum(arr)/len(arr):0.1f}')