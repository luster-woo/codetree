from collections import deque

n, m = map(int, input().split())
a = deque()
b = deque()

# A 입력
for _ in range(n):
    d, cnt = input().split()
    a.append([d, int(cnt)])

# B 입력
for _ in range(m):
    d, cnt = input().split()
    b.append([d, int(cnt)])

pos_a = 0
pos_b = 0
time = 0

while a and b:
    d1, c1 = a.popleft()
    d2, c2 = b.popleft()

    # 동시에 한 칸씩 이동
    step = min(c1, c2)

    for _ in range(step):
        time += 1

        if d1 == 'R':
            pos_a += 1
        else:
            pos_a -= 1

        if d2 == 'R':
            pos_b += 1
        else:
            pos_b -= 1

        if pos_a == pos_b:
            print(time)
            exit()
    if c1 > step:
        a.appendleft([d1, c1 - step])
    if c2 > step:
        b.appendleft([d2, c2 - step])

print(-1)