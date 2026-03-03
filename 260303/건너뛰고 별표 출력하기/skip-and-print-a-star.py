n = int(input())

# 위쪽 (1 ~ n)
for i in range(1, n + 1):
    print("*" * i)
    print()

# 아래쪽 (n-1 ~ 1)
for i in range(n - 1, 0, -1):
    print("*" * i)
    print()