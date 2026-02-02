a, b = map(int, input().split())
cnt = 0

for i in range(a, b+1):
    c = i % 10
    d = i // 10
    if i % 3 == 0 or c in [3,6,9] or d in [3,6,9]:
        cnt += 1

print(cnt)
