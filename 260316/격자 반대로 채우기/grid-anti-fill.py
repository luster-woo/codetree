n = int(input())

arr = [[0]*n for _ in range(n)]
cnt = 1

for x in range(n-1, -1, -1):
    if (n-1-x) % 2 == 0:  # 아래 -> 위
        for y in range(n-1, -1, -1):
            arr[y][x] = cnt
            cnt += 1
    else:                 # 위 -> 아래
        for y in range(n):
            arr[y][x] = cnt
            cnt += 1

for row in arr:
    print(*row)