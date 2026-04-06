import sys
input = sys.stdin.readline

# 좌표 평면 설정 (offset 포함)
visited = [[0]*2001 for _ in range(2001)]
offset = 1000

# 첫 번째 사각형 (잔해물 생성)
x1, y1, x2, y2 = map(int, input().split())
for x in range(x1 + offset, x2 + offset):
    for y in range(y1 + offset, y2 + offset):
        visited[x][y] = 1

# 두 번째 사각형 (잔해물 제거)
x3, y3, x4, y4 = map(int, input().split())
for x in range(x3 + offset, x4 + offset):
    for y in range(y3 + offset, y4 + offset):
        visited[x][y] = 0

# 남아있는 잔해물의 최소/최대 좌표 찾기
min_x, max_x = 2001, -1
min_y, max_y = 2001, -1
exist = False

for x in range(2001):
    for y in range(2001):
        if visited[x][y] == 1:
            exist = True
            if x < min_x: min_x = x
            if x > max_x: max_x = x
            if y < min_y: min_y = y
            if y > max_y: max_y = y

# 결과 출력
if not exist:
    print(0)
else:
    # 좌표 기반이므로 (max - min + 1)이 실제 변의 길이가 됨
    width = max_x - min_x + 1
    height = max_y - min_y + 1
    print(width * height)