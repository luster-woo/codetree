def recur(n,cnt):
    if n==1:
        return cnt
    else:
        if n%2==0:
            return recur(n//2,cnt+1)
        else:
            return recur(n*3+1,cnt+1)
n = int(input())
print(recur(n,0))
# Please write your code here.