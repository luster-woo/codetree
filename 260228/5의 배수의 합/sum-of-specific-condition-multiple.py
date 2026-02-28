a,b = map(int,input().split())
result = 0
if a<=b:
    for x in range(a,b+1):
        if x%5==0:
            result+=x
else:
    for x in range(b,a+1) :
        if x%5==0:
            result+=x
print(result)