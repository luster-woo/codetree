n, k, p, t = map(int, input().split())

arr = []
for _ in range(t):
    time, x, y = map(int, input().split())
    arr.append((time, x, y))

# 시간순 정렬
arr.sort(key=lambda x: x[0])

infected = [0] * n
remain = [0] * n

infected[p-1] = 1
remain[p-1] = k

for _, x, y in arr:
    x -= 1
    y -= 1

    # 이전 상태 저장 (핵심)
    x_inf = infected[x]
    y_inf = infected[y]

    # 감염 전파
    if x_inf and remain[x] > 0:
        infected[y] = 1
    if y_inf and remain[y] > 0:
        infected[x] = 1

    # 횟수 감소 (감염자면 무조건)
    if x_inf and remain[x] > 0:
        remain[x] -= 1
    if y_inf and remain[y] > 0:
        remain[y] -= 1

# 출력
for i in range(n):
    print(infected[i], end="")