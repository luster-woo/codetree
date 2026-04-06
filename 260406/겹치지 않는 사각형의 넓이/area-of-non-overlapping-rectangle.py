import sys
input = sys.stdin.readline
visited = [[0]*2001 for _ in range(2001)]
offset = 1000
for _ in range(2):
    a,b,c,d = map(int,input().split())
    for x in range(a+offset,c+offset):
        for y in range(b+offset,d+offset):
            visited[x][y]=1
a,b,c,d = map(int,input().split())
for x in range(a+offset,c+offset):
    for y in range(b+offset,d+offset):
        visited[x][y]=0
result = 0 
for x in range(2000):
    for y in range(2000):
        if visited[x][y]==1:
            result+=1
print(result)