n = int(input())
for x in range(2*n+1):
    for y in range(2*n+1):
        if x%2==0:
            print("* ",end="")
        else:
            for _ in range(n+1):
                print("*   ",end="")
            break
    print()