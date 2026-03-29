def recur(n):
    if n==1:
        return 1
    elif n==2:
        return 2
    else:
        return recur(n//3)+recur(n-1)
N = int(input())
print(recur(N))
# Please write your code here.