a, b = map(int, input().split())
cnt = 0
for i in range(a,b+1):
    c = i%10 
    d = i//10
    if i%3==0 or c%3==0 or d%3==0:
        cnt +=1
print(cnt)