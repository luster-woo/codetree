a,b = map(int,input().split())
result = 0
for x in range(a,b+1):
    if x%2==0:
        result+=x
print(result)