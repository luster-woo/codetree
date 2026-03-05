# 정수 N 입력 받기
n = int(input())

# 행(i) 반복: 1부터 n까지
for i in range(1, n + 1):
    # 열(j) 반복: n부터 1까지 역순으로
    for j in range(n, 0, -1):
        print(i * j, end=" ")
    # 한 줄이 끝나면 줄바꿈
    print()