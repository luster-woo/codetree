n = int(input())
for x in range(1,n):
    n//=x
    if n<=1:
        print(x)
        break
