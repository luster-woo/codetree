n = int(input())

# 위쪽 (1부터 n까지)
for i in range(1, n+1):
    print(" " * (n - i) + "*" * (2*i - 1))

# 아래쪽 (n-1부터 1까지)
for i in range(n-1, 0, -1):
    print(" " * (n - i) + "*" * (2*i - 1))