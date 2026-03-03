n = int(input())
for x in range(n):
    print("  "*x,end="")
    print("* "*(2*(n-x)-1))