arr = input()

cnt = 0
for i in range(len(arr)-1):
    if arr[i:i+2] == 'ee':
        cnt += 1
print(cnt, end=" ")

cnt = 0
for i in range(len(arr)-1):
    if arr[i:i+2] == 'eb':
        cnt += 1
print(cnt)