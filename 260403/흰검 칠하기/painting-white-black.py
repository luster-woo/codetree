import sys

# 명령의 수 N 입력
n = int(input())

# 타일 상태 추적을 위한 딕셔너리
# {위치: [흰색_횟수, 검은색_횟수, 마지막_색]}
# 마지막_색: 0(흰색), 1(검은색)
tiles = {}
curr = 0

for _ in range(n):
    line = input().split()
    x = int(line[0])
    direction = line[1]
    
    if direction == 'L':
        # 왼쪽으로 x칸 (현재 칸 포함)
        for i in range(curr, curr - x, -1):
            if i not in tiles:
                tiles[i] = [0, 0, 0]
            
            # 이미 회색이 된 타일이 아니라면 카운트 증가
            if not (tiles[i][0] >= 2 and tiles[i][1] >= 2):
                tiles[i][0] += 1
                tiles[i][2] = 0 # 마지막 색: 흰색
        curr = curr - x + 1
        
    else: # direction == 'R'
        # 오른쪽으로 x칸 (현재 칸 포함)
        for i in range(curr, curr + x):
            if i not in tiles:
                tiles[i] = [0, 0, 1]
            
            if not (tiles[i][0] >= 2 and tiles[i][1] >= 2):
                tiles[i][1] += 1
                tiles[i][2] = 1 # 마지막 색: 검은색
        curr = curr + x - 1

# 결과 집계
w_cnt, b_cnt, g_cnt = 0, 0, 0

for pos in tiles:
    w_num, b_num, last_color = tiles[pos]
    
    if w_num >= 2 and b_num >= 2:
        g_cnt += 1
    elif last_color == 0:
        w_cnt += 1
    elif last_color == 1:
        b_cnt += 1

print(w_cnt, b_cnt, g_cnt)