result = 0
n = int(input())
for x in range(1,n):
    if n%x==0:
        result+=x
if result == n:
    print("P")
else:
    print("N")