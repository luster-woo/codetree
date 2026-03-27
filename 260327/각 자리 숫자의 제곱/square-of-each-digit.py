def square(n):
    if n==0:
        return 0
    else:
        return square(n//10)+((n%10)**2)
N = int(input())
print(square(N))
# Please write your code here.