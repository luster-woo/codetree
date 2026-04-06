n = int(input())
x1, y1, x2, y2 = [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    x1.append(a)
    y1.append(b)
    x2.append(c)
    y2.append(d)
visited = [[0]*201 for _ in range(201)]
offset = 100
for x in range(n):
    a,b,c,d = x1[x],y1[x],x2[x],y2[x]
    if x%2==0:
        for x in range(a+offset,c+offset):
            for y in range(b+offset,d+offset):
                visited[x][y]=1
    else:
        for x in range(a+offset,c+offset):
            for y in range(b+offset,d+offset):
                visited[x][y]=2
result = 0  
for x in range(201):
    for y in range(201):
        if visited[x][y]==2:
            result+=1
print(result)