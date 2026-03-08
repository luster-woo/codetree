N = int(input())

for i in range(N, 0, -1):
    print("  " * (N - i), end="")
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()