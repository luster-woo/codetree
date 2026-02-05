def cut(arr, n):
    for i in range(n):
        if arr[i] % 2 == 0:
            arr[i] //= 2
    return arr

n = int(input())
arr = list(map(int, input().split()))
result = cut(arr, n)
for i in range(n):
    print(result[i], end=" ")
