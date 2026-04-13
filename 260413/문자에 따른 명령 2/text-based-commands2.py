dirs = input()

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

i = 0  # 북쪽 시작
x, y = 0, 0

for d in dirs:
    if d == "L":
        i = (i - 1) % 4
    elif d == "R":
        i = (i + 1) % 4
    else:  # F
        x += dx[i]
        y += dy[i]

print(x, y)