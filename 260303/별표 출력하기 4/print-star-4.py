n = int(input())

for i in range(1, n + 1):
    print("* " * (n-i+1))

# 아래쪽 (n-1 ~ 1)
for i in range(n - 1, 0, -1):
    print("* " * (n-i+1))