n, m = map(int, input().split())

arr = [[0]*m for _ in range(n)]
cnt = 1

for s in range(n + m - 1):   # 대각선 번호
    for i in range(n):
        j = s - i
        if 0 <= j < m:
            arr[i][j] = cnt
            cnt += 1

for x in arr:
    print(*x)