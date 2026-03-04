n = int(input())

# 위쪽
for i in range(1, n+1):
    print("  " * (n-i) + "@ " * i)

# 아래쪽
for i in range(n-1, 0, -1):
    print("@ " * i)