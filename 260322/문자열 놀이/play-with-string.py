arr, cnt = map(str,input().split())
arr =list(arr)
cnt = int(cnt)
for _ in range(cnt):
    a,b,c = map(str,input().split())
    a = int(a)
    if a==1:
        b,c = int(b),int(c)
        arr[b-1],arr[c-1]=arr[c-1],arr[b-1]
        print(''.join(arr))
    else:
        for i in range(len(arr)):
            if arr[i] == b:
                arr[i] = c
        print(''.join(arr))
