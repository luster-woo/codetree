m1, d1, m2, d2 = map(int, input().split())
target = input().strip()

days = [31,29,31,30,31,30,31,31,30,31,30,31]

# 날짜를 "연초 기준"으로 변환
def get_day(m, d):
    return sum(days[:m-1]) + d

start = get_day(m1, d1)
end = get_day(m2, d2)

# 요일 배열
days_name = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

count = 0

for i in range(end - start + 1):  # 시작 포함
    current_day = days_name[i % 7]
    if current_day == target:
        count += 1

print(count)