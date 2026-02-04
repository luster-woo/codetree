
def is_validation(y, m, d):
    if y < 0 or m <= 0 or m > 12 or d < 1 or d > 31:
        return "-1"

    # 윤년
    if y % 4 == 0 and (y % 100 != 0 or y % 400 == 0):
        if m == 3 or m == 5:
            return "Spring"
        elif m == 1 or m == 12:
            return "Winter"
        elif m == 7 or m == 8:
            return "Summer"
        elif m == 10:
            return "Fall"
        elif m == 4 and d <= 30:
            return "Spring"
        elif m == 6 and d <= 30:
            return "Summer"
        elif (m == 9 or m == 11) and d <= 30:
            return "Fall"
        elif m == 2 and d <= 29:
            return "Winter"
        else:
            return "-1"

    # 평년
    else:
        if m == 3 or m == 5:
            return "Spring"
        elif m == 1 or m == 12:
            return "Winter"
        elif m == 7 or m == 8:
            return "Summer"
        elif m == 10:
            return "Fall"
        elif m == 4 and d <= 30:
            return "Spring"
        elif m == 6 and d <= 30:
            return "Summer"
        elif (m == 9 or m == 11) and d <= 30:
            return "Fall"
        elif m == 2 and d <= 28:
            return "Winter"
        else:
            return "-1"


y, m, d = map(int, input().split())
result = is_validation(y,m,d)
print(result)

