n = int(input())
cnt = 0
arr = []
i=1
while cnt<2:
    if (n*i)%5==0:
        cnt+=1
    arr.append(n*i)
    i+=1
print(*arr)