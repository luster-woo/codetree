a,b = map(int ,input().split())
for x in range(max(a,b),min(a,b)-1,-1):
    print(x,end=" ")