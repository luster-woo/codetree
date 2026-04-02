m1, d1, m2, d2 = map(int, input().split())

# 2011년 각 달의 일수 (윤년 아님)
days = [31,28,31,30,31,30,31,31,30,31,30,31]

# 같은 달인 경우
if m1 == m2:
    print(d2 - d1 + 1)
else:
    # 첫 달 남은 날짜
    result = days[m1-1] - d1 + 1
    
    # 중간 달들
    for m in range(m1, m2-1):
        result += days[m]
    
    # 마지막 달
    result += d2
    
    print(result)