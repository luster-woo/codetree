N = int(input())

current_num = 1  # 출력할 시작 숫자

for i in range(N):
    # 1. 각 행의 시작 부분에 공백 출력 (행 번호만큼 공백 추가)
    print("  " * i, end="")
    
    # 2. 각 행에서 출력할 숫자의 개수는 N, N-1, N-2 ... 순서
    for j in range(N - i):
        print(current_num, end=" ")
        
        # 숫자 증가 및 1~9 순환 로직
        current_num += 1
        if current_num > 9:
            current_num = 1
            
    # 3. 한 행 출력이 끝나면 줄바꿈
    print()