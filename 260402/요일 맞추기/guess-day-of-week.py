m1, d1, m2, d2 = map(int, input().split())

days = [31,28,31,30,31,30,31,31,30,31,30,31]

# 해당 날짜를 "연초부터 몇 번째 날"로 변환
def get_day(m, d):
    return sum(days[:m-1]) + d

start = get_day(m1, d1)
end = get_day(m2, d2)

diff = end - start  # 음수 가능!

days_name = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

# 파이썬에서는 음수 % 7도 정상 작동함
print(days_name[diff % 7])