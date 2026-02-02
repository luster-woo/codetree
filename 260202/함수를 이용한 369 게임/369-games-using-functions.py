a, b = map(int, input().split())
cnt = 0

for i in range(a, b+1):
    if i % 3 == 0:
        cnt += 1
    else:
        s = str(i)
        if '3' in s or '6' in s or '9' in s:
            cnt += 1

print(cnt)
