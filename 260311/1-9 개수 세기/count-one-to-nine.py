n = int(input())
dict={}
arr =list(map(int,input().split()))
for i in range(1,10):
    cnt = 0
    for x in arr:
        if x == i:
            cnt+=1
    print(cnt)