import sys
input = sys.stdin.readline

n = int(input())
events = []

for _ in range(n):
    x1, x2 = map(int, input().split())
    events.append((x1, 1))   # 시작
    events.append((x2, -1))  # 끝

# 정렬: 좌표 기준, 같으면 끝(-1)이 먼저
events.sort(key=lambda x: (x[0], x[1]))

cur = 0
max_val = 0

for x, val in events:
    cur += val
    max_val = max(max_val, cur)

print(max_val)