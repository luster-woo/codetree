arr = list(map(int,input().split()))

for i in range(1,10):
    cnt = 0
    for x in arr:
        if x != 0 and x//10 == i:
            cnt += 1
    print(f'{i} - {cnt}')