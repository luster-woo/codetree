import sys
input = sys.stdin.readline
visited = [[0]*2001 for _ in range(2001)]
offset = 1000
a,b,c,d = map(int,input().split())
for x in range(a+offset,c+offset):
    for y in range(b+offset,d+offset):
        visited[x][y]=1
a,b,c,d = map(int,input().split())
for x in range(a+offset,c+offset):
    for y in range(b+offset,d+offset):
        visited[x][y]=0
result = 0 
max_x = 0
max_y = 0
for x in range(2000):
    temp  = 0
    temp_1  = 0
    for y in range(2000):
        if visited[x][y]==1:
            temp+=1
        else:
            max_x = max(max_x,temp)
            temp = 0
        if visited[y][x]==1:
            temp_1+=1
        else:
            max_y = max(max_y,temp_1)
            temp_1 = 0
    
print(max_x*max_y)