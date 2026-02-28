n = int(input())
cnt = 0
for _ in range(n):
    a = int(input())
    if a%3==0 and a%2==1:
        cnt+=a
print(cnt)