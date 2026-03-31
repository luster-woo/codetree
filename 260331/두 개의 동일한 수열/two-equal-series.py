n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A= set(A)
B= set(B)
if A==B:
    print("Yes")
else:
    print("No")