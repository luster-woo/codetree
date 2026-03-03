N = int(input())

for i in range(N):
    left = "*" * (N - i)
    space = " " * (2 * i)
    right = "*" * (N - i)
    print(left + space + right)