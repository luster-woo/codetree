a,b,c = map(int,input().split())
for x in range(a,b+1):
    if x%c==0:
        print("YES")
        exit()
print("NO")