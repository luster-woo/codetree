# 입력 전체를 리스트로 받습니다.
arr = list(map(int, input().split()))

# 1부터 9까지(십의 자리 숫자들) 반복
for i in range(1, 10):
    cnt = 0
    for x in arr:
        # 0이 나오면 그 이후는 계산하지 않고 멈춤 (문제 조건)
        if x == 0:
            break
        
        # 10 이상인 숫자만 대상으로 (한 자리 수 제외 조건)
        if x >= 10:
            # 십의 자리 숫자 추출 (x가 99 이하이므로 x // 10이면 충분)
            if (x // 10) == i:
                cnt += 1
                
    print(f"{i} - {cnt}")