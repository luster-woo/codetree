n = int(input())
for x in range(1,n+1):
    if x%2!=0 and (x%3!=0 or x%9==0) and (x%5!=0 or x%10==0):
        print(x,end=" ")
