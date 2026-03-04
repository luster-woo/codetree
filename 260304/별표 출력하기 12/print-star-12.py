n = int(input())

# 1. 첫 번째 줄 출력
for j in range(1, n + 1):
    print("*", end=" ")
print()

# 2. 두 번째 줄부터 N번째 줄까지 출력
for i in range(2, n + 1):
    for j in range(1, n + 1):
        # 규칙: 맨 마지막 열(j==n)이거나, 
        # 열 번호(j)가 짝수이면서 현재 행(i)보다 크거나 같을 때
        if j % 2 == 0 and j >= i:
            print("*", end=" ")
        else:
            print("  ", end="")
    print()