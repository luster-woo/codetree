n, m  = map(str, input().split())
n = int(n)
cnt = 0
for _ in range(n):
    temp  = input()
    if m==temp:
        cnt+=1
print(cnt)