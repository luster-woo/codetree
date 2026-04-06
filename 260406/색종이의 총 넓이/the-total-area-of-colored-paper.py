import sys
input = sys.stdin.readline
visited = [[0]*201 for _ in range(201)]
offset = 100
n = int(input())
for _ in range(n):
    a,b = map(int,input().split())
    for x in range(a+offset,a+offset+8):
        for y in range(b+offset,b+offset+8):
            visited[x][y]=1
result = 0 
for x in range(201):
    for y in range(201):
        if visited[x][y]==1:
            result+=1
print(result)