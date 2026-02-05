n = int(input())
arr = list(map(int, input().split()))
def abc(arr,n):
    for i in range(n):
        arr[i]=abs(arr[i])
    return arr
arr = abc(arr,len(arr))
for i in range(len(arr)):
    print(arr[i], end=" ")