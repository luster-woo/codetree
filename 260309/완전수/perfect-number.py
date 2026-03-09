s, e = map(int, input().split())
cnt = 0
for x in range(s,e+1):
    result = 0
    for y in range(1,x):
        if x%y==0:
            result+=y
    if result==x:
        cnt+=1
print(cnt)
