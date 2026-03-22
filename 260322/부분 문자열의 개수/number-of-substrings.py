arr = input()
target = input()
cnt = 0
for i in range(len(arr)-len(target)+1):
    if arr[i:i+len(target)] == target:
        cnt+=1
print(cnt)