import sys
input = sys.stdin.readline

n = int(input())

arr = [0] * 2001
cur = 1000  # 0 위치를 가운데로

for _ in range(n):
    x, d = input().split()
    x = int(x)

    if d == 'R':
        for i in range(cur, cur + x):
            arr[i] += 1
        cur += x
    else:
        for i in range(cur - x, cur):
            arr[i] += 1
        cur -= x

cnt = 0
for v in arr:
    if v >= 2:
        cnt += 1

print(cnt)