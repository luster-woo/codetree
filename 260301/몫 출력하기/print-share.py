count = 0  # 짝수 출력 횟수

while True:
    num = int(input())
    
    if num % 2 == 0:      # 짝수이면
        print(num // 2)
        count += 1
    
    if count == 3:        # 3번 출력하면 종료
        break