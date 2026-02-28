result = 0
cnt= 0
a,b = map(int,input().split())
for x in range(a,b+1):
    if x%5==0 or x%7==0:
        result+=x
        cnt+=1
print(f'{result} {result/cnt:0.1f}')