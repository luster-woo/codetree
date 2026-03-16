n, m = map(int, input().split())

cnt = 0
arr = [[0]*m for _ in range(n)]

for x in range(m):
    for y in range(n):
        if x % 2 == 0:
            arr[y][x] = cnt
        else:
            arr[n-y-1][x] = cnt
        cnt += 1

for x in arr:
    print(*x)