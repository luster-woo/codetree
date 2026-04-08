from collections import deque

n, m = map(int, input().split())
a = deque()
b = deque()

# A 입력
for _ in range(n):
    cnt, d = input().split()
    a.append([d, int(cnt)])

# B 입력
for _ in range(m):
    cnt, d = input().split()
    b.append([d, int(cnt)])

pos_a = 0
pos_b = 0

prev_same = True  # 처음은 같은 위치 (카운트 X)
answer = 0

while a or b:
    if a:
        d1, c1 = a.popleft()
    else:
        d1, c1 = 'R', 0

    if b:
        d2, c2 = b.popleft()
    else:
        d2, c2 = 'R', 0

    step = max(c1, c2)

    for _ in range(step):
        if c1 > 0:
            pos_a += 1 if d1 == 'R' else -1
            c1 -= 1

        if c2 > 0:
            pos_b += 1 if d2 == 'R' else -1
            c2 -= 1

        # 현재 같은지 체크
        if pos_a == pos_b:
            if not prev_same:
                answer += 1
            prev_same = True
        else:
            prev_same = False

    if c1 > 0:
        a.appendleft([d1, c1])
    if c2 > 0:
        b.appendleft([d2, c2])

print(answer)