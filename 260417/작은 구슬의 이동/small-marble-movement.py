n, t = map(int, input().split())
r, c, d = input().split()
r, c = int(r), int(c)

# 방향 정의: 상(U), 하(D), 우(R), 좌(L)
# 문제의 R, C 좌표계에 맞게 행(dr), 열(dc) 변화량 설정
mapper = {
    'U': (-1, 0),
    'D': (1, 0),
    'R': (0, 1),
    'L': (0, -1)
}

# 반대 방향 전환용 매퍼
opposite = {
    'U': 'D', 'D': 'U', 'R': 'L', 'L': 'R'
}

dr, dc = mapper[d]

for _ in range(t):
    nr, nc = r + dr, c + dc
    
    # 격자 범위를 벗어나는지 확인
    if 1 <= nr <= n and 1 <= nc <= n:
        # 이동 가능한 경우: 위치 갱신
        r, c = nr, nc
    else:
        # 이동 불가능한 경우 (벽): 방향만 반대로 전환 (1초 소모)
        d = opposite[d]
        dr, dc = mapper[d]

print(r, c)