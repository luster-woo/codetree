n = int(input())

for i in range(n): # i는 행(Row)
    for j in range(n): # j는 열(Column)
        if j % 2 == 0:
            # 홀수 번째 열 (0, 2...) : 위에서 아래로 1, 2, 3, 4
            print(i + 1, end="")
        else:
            # 짝수 번째 열 (1, 3...) : 아래에서 위로 1, 2, 3, 4 (위에서 보면 4, 3, 2, 1)
            print(n - i, end="")
    print() # 줄바꿈