arr = input()
target = input()
flag = False
for i in range(len(arr)-1):
    if arr[i:i+len(target)] == target:
        print(i)
        flag = True
        break
if not flag:
    print(-1)
