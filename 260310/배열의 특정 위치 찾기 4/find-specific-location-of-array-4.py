arr = list(map(int,input().split()))

if 0 in arr:
    arr = arr[:arr.index(0)]
cnt = 0
result = 0
for x in arr:
    if x%2==0:
        cnt+=1
        result+=x
print(cnt,result)