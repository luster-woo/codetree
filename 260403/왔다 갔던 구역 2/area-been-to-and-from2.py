import sys
input = sys.stdin.readline

n = int(input())
arr = [0]*2001  # 넉넉하게
start = 1000    # 가운데 시작

for _ in range(n):
    dist, dir = input().split()
    dist = int(dist)

    if dir == "R":
        for x in range(1, dist+1):   # 1부터!
            arr[start + x] += 1
        start += dist
    else:
        for x in range(1, dist+1):   # 1부터!
            arr[start - x] += 1
        start -= dist

cnt = 0
for x in arr:
    if x >= 2:
        cnt += 1

print(cnt)