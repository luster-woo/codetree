n, k, p, t = map(int, input().split())

arr = []
for _ in range(t):
    time, x, y = map(int, input().split())
    arr.append((time, x-1, y-1))

arr.sort()

infected = [0]*n
remain = [0]*n

infected[p-1] = 1
remain[p-1] = k

for _, x, y in arr:
    x_inf = infected[x]
    y_inf = infected[y]

    # 전염
    if x_inf and remain[x] > 0:
        if infected[y] == 0:
            remain[y] = k   # 🔥 추가
        infected[y] = 1

    if y_inf and remain[y] > 0:
        if infected[x] == 0:
            remain[x] = k   # 🔥 추가
        infected[x] = 1

    # 횟수 감소
    if x_inf and remain[x] > 0:
        remain[x] -= 1
    if y_inf and remain[y] > 0:
        remain[y] -= 1

print("".join(map(str, infected)))