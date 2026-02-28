a,b = map(int,input().split())
result =1
for x in range(1,b+1):
    if x%a==0:
        result*=x
print(result)