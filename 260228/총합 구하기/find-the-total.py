result = 0
a,b = map(int,input().split())
for x in range(a,b+1):
    if x%6==0 and x%8!=0:
        result+=x
print(result)