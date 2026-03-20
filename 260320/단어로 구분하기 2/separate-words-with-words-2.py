arr = list(input().split(" "))
cnt = 0
for x in arr:
    if cnt%2==0:
        print(x)
    cnt+=1