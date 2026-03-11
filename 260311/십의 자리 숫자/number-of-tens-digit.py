arr = list(map(int,input().split()))
arr.pop()

for i in range(1,10):
    cnt = 0
    for x in arr:
        if x>=10 and (x//10)%10 == i:
            cnt += 1
    print(f'{i} - {cnt}')