arr = [0]*10
arr[0] =2
arr[1] = 5
for i in range(2,10):
    arr[i]= (arr[i-1]+arr[i-2])%10
print(*arr)