def fibo(n):
    if n==1 or n==2:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)

N = int(input())
print(fibo(N))
# Please write your code here.