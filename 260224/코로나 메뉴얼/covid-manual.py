cnt = 0
for _ in range(3):
    arr = list(map(str,input().split()))
    if arr[0]=='Y' and int(arr[1])>=37:
        cnt+=1
if cnt>=2:
    print("E")
else:
    print("N")