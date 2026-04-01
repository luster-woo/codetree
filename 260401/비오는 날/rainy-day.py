class Weather:
    def __init__(self, date, day, weather):
        self.date = date
        self.day = day
        self.weather = weather


n = int(input())
data = []

# 입력
for _ in range(n):
    date, day, weather = input().split()
    data.append(Weather(date, day, weather))

# 비 오는 날만 필터링
rainy = [d for d in data if d.weather == "Rain"]

# 가장 빠른 날짜 찾기 (문자열 비교로 가능: YYYY-MM-DD 형태라고 가정)
target = min(rainy, key=lambda x: x.date)

# 출력
print(target.date, target.day, target.weather)