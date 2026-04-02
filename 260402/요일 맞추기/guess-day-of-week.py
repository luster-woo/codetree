m1, d1, m2, d2 = map(int, input().split())

# 각 달 일수
days = [31,28,31,30,31,30,31,31,30,31,30,31]

# 날짜 차이 계산 (시작일 제외)
diff = 0

if m1 == m2:
    diff = d2 - d1
else:
    # 첫 달 남은 일수
    diff += days[m1-1] - d1
    
    # 중간 달
    for m in range(m1, m2-1):
        diff += days[m]
    
    # 마지막 달
    diff += d2

# 요일 계산
days_name = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

result = days_name[diff % 7]
print(result)