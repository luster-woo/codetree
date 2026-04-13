import sys
input = sys.stdin.readline

n, m = map(int, input().split())

A = []
B = []

for _ in range(n):
    v, t = map(int, input().split())
    for _ in range(t):
        if A:
            A.append(A[-1] + v)
        else:
            A.append(v)

for _ in range(m):
    v, t = map(int, input().split())
    for _ in range(t):
        if B:
            B.append(B[-1] + v)
        else:
            B.append(v)

max_len = max(len(A), len(B))

while len(A) < max_len:
    A.append(A[-1])
while len(B) < max_len:
    B.append(B[-1])

def state(a, b):
    if a > b:
        return 1
    elif a < b:
        return -1
    else:
        return 0

cnt = 0
prev = state(A[0], B[0])

for i in range(1, max_len):
    now = state(A[i], B[i])
    if now != prev:
        cnt += 1
        prev = now

print(cnt+1)