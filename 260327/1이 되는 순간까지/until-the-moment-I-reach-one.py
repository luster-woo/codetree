def search(n,cnt):
    if n==1:
        return cnt 
    elif n%2==0:
        return search(n//2,cnt+1)
    else:
        return search(n//3,cnt+1)
N = int(input())
print(search(N,0))
# Please write your code here.