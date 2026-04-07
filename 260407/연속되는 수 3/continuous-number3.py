n = int(input())
arr = []
for _ in range(n):
    temp = int(input())
    arr.append(temp)
max_val = 0
temp = 1
for x in range(len(arr)-1):
    if (arr[x]>0 and arr[x+1]<0) or (arr[x]<0 and arr[x+1]>0):
        max_val = max(max_val,temp)
        temp = 1
    else:
        temp+=1
max_val = max(max_val,temp)
print(max_val)