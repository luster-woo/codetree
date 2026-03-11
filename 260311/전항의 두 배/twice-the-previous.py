arr = []
a,b = map(int,input().split())
arr.append(a)
arr.append(b)
i =2
while len(arr)<10:
    arr.append(2*arr[i-2]+arr[i-1])
    i+=1
print(*arr)