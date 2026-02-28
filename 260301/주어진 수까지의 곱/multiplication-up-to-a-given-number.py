prod = 1
a,b = map(int,input().split())
for x in range(a,b+1):
    prod*=x
print(prod)