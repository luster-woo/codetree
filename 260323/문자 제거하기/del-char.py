arr = list(input())

while len(arr) > 1:
    n = int(input())
    
    if 0 <= n < len(arr):
        arr.pop(n)
        print(''.join(arr))
    else:
        print(arr[0])
        break