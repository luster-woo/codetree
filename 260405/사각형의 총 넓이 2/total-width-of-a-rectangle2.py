from collections import Counter

N = int(input())
rects = [tuple(map(int, input().split())) for _ in range(N)]

events = []
for x1, y1, x2, y2 in rects:
    events.append((x1, 1, y1, y2))  # 사각형 시작
    events.append((x2, -1, y1, y2)) # 사각형 끝

events.sort()
active = Counter()
prev_x = events[0][0]
total_area = 0

for x, typ, y1, y2 in events:
    # 현재 활성화된 y 구간 계산
    intervals = []
    for (a,b), cnt in active.items():
        if cnt > 0:
            intervals.append((a,b))
    intervals.sort()
    
    merged = []
    for a, b in intervals:
        if not merged or merged[-1][1] < a:
            merged.append([a, b])
        else:
            merged[-1][1] = max(merged[-1][1], b)
    
    y_total = sum(b-a for a,b in merged)
    total_area += y_total * (x - prev_x)
    
    active[(y1,y2)] += typ
    prev_x = x

print(total_area)