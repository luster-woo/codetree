a,b = map(int,input().split())
result = str(a+b)
result = list(result)
cnt = 0
for x in result:
    if x=='1':
        cnt+=1
print(cnt)