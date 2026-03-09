n = int(input())
for _ in range(n):
    a,b = map(int,input().split())
    result =1
    for x in range(a,b+1):
        result*=x
    print(result)