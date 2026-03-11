a,b = map(int,input().split())
cnt = 0
arr = [a,b]
while len(arr)<10:
    temp = arr[len(arr)-2] + arr[len(arr)-1]
    temp %=10
    arr.append(temp)
print(*arr)