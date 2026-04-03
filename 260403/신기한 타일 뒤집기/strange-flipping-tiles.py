import sys

# 명령의 수 N 입력
n = int(input())

# 타일 상태를 저장할 딕셔너리 (위치: 색깔)
# 색깔: 0(흰색), 1(검은색)
tiles = {}
curr = 0 # 시작 위치

for _ in range(n):
    line = input().split()
    x = int(line[0])
    direction = line[1]
    
    if direction == 'L':
        # 현재 위치 포함 왼쪽으로 x칸 뒤집기
        # range(start, stop, step)
        for i in range(curr, curr - x, -1):
            tiles[i] = 0 # 흰색으로 변경
        # 마지막으로 뒤집은 타일 위치로 업데이트
        curr = curr - x + 1
        
    else: # direction == 'R'
        # 현재 위치 포함 오른쪽으로 x칸 뒤집기
        for i in range(curr, curr + x):
            tiles[i] = 1 # 검은색으로 변경
        # 마지막으로 뒤집은 타일 위치로 업데이트
        curr = curr + x - 1

# 결과 집계
white_count = 0
black_count = 0

for color in tiles.values():
    if color == 0:
        white_count += 1
    else:
        black_count += 1

print(white_count, black_count)