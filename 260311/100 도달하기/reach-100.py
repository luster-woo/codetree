arr = []*100
arr.append(1)
n = int(input())
arr.append(n)
i=2
while True:
    temp=arr[i-1]+arr[i-2]
    arr.append(temp)
    i+=1
    if temp>100:
        break
print(*arr)