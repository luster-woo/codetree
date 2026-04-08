from collections import deque

n, m = map(int, input().split())
a = deque()
b = deque()

# A 입력
for _ in range(n):
    v, t = map(int, input().split())
    a.append([v, t])

# B 입력
for _ in range(m):
    v, t = map(int, input().split())
    b.append([v, t])

pos_a = 0
pos_b = 0

prev = 0  # 이전 선두
answer = 0

while a and b:
    v1, t1 = a.popleft()
    v2, t2 = b.popleft()

    step = min(t1, t2)

    for _ in range(step):
        pos_a += v1
        pos_b += v2

        if pos_a > pos_b:
            cur = 1
        elif pos_a < pos_b:
            cur = -1
        else:
            cur = 0

        if cur != 0:
            if prev != 0 and prev != cur:
                answer += 1
            prev = cur

    if t1 > step:
        a.appendleft([v1, t1 - step])
    if t2 > step:
        b.appendleft([v2, t2 - step])

print(answer)