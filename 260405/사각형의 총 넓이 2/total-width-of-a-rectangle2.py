N = int(input())
rects = []
for _ in range(N):
    x1, y1, x2, y2 = map(int, input().split())
    rects.append((x1, y1, x2, y2))

events = []
for x1, y1, x2, y2 in rects:
    events.append((x1, 1, y1, y2))  # 사각형 시작
    events.append((x2, -1, y1, y2)) # 사각형 끝

events.sort()  # x 기준 정렬

import bisect

active = []
prev_x = events[0][0]
total_area = 0

for x, typ, y1, y2 in events:
    # 현재 활성화된 y 구간의 총 길이 계산
    active.sort()
    merged = []
    for a, b in active:
        if not merged or merged[-1][1] < a:
            merged.append([a, b])
        else:
            merged[-1][1] = max(merged[-1][1], b)
    y_total = sum(b-a for a,b in merged)
    
    total_area += y_total * (x - prev_x)
    
    if typ == 1:
        active.append([y1, y2])
    else:
        active.remove([y1, y2])
    
    prev_x = x

print(total_area)