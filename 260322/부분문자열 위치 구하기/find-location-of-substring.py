arr = input()
target = input()
flag = False
for i in range(len(arr)-len(target)):
    if arr[i:i+len(target)] == target:
        print(i)
        flag = True
        break
if not flag:
    print(-1)
