n = int(input())

# N이 1인 경우 예외 처리
if n == 1:
    print("*")
else:
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            # 1. 첫 줄이나 마지막 줄인 경우
            # 2. 첫 열이나 마지막 열인 경우
            # 3. 열 번호(j)가 행 번호(i)보다 작거나 같은 경우 (단, 공백 규칙 확인)
            if i == 1 or i == n or j == 1 or j == n or j <= i - 1:
                print("*", end=" ")
            else:
                print("  ", end="")
        print()