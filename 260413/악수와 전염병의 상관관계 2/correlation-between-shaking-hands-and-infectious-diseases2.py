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

i = 0
while i < t:
    j = i

    # 같은 시간 묶기
    while j < t and arr[j][0] == arr[i][0]:
        j += 1

    # 이번 시간에 일어나는 악수들
    temp = []

    for idx in range(i, j):
        _, x, y = arr[idx]

        if infected[x] and remain[x] > 0:
            temp.append((x, y))
        if infected[y] and remain[y] > 0:
            temp.append((y, x))

    # 감염 반영
    for x, y in temp:
        infected[y] = 1

    # 횟수 감소
    for idx in range(i, j):
        _, x, y = arr[idx]

        if infected[x] and remain[x] > 0:
            remain[x] -= 1
        if infected[y] and remain[y] > 0:
            remain[y] -= 1

    i = j

print("".join(map(str, infected)))