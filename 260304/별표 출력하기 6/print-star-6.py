n = int(input())

# 위쪽 (큰 -> 작은)
for x in range(n, 0, -1):
    print("  "*(n-x), end="")
    print("* "*(2*x-1))

# 아래쪽 (작은 -> 큰)
for y in range(2, n+1):
    print("  "*(n-y), end="")
    print("* "*(2*y-1))