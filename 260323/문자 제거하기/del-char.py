arr = list(input())

while len(arr) > 1:
    n = int(input())
    
    if 0 <= n < len(arr):
        arr.pop(n)
        print(''.join(arr))
    else:
        arr.pop(len(arr)-1)
        print(''.join(arr))
