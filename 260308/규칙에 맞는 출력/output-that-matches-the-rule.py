N = int(input())

# 1부터 N까지 반복 (i는 현재 몇 번째 행인지를 나타냄)
for i in range(1, N + 1):
    # 각 행의 시작 숫자는 N - i + 1
    start_num = N - i + 1
    
    # 시작 숫자부터 N까지 숫자를 출력
    for j in range(start_num, N + 1):
        print(j, end=" ")
        
    # 한 행이 끝나면 줄바꿈
    print()