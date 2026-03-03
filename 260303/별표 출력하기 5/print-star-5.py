n = int(input())
for x in range(n):
    for y in range(n-x):
        print("*"*(n-x),end=" ")
    print()