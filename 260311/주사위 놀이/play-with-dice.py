arr =list(map(int,input().split()))
for i in range(1,7):
    cnt = 0
    for x in arr:
        if x == i:
            cnt+=1
    print(f'{i} - {cnt}')