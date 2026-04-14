n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
dx = [0,1,0,-1]
dy = [1,0,-1,0]
result = 0
for x in range(n):
    for y in range(n):
        cnt = 0
        for i in range(4):
            ni = x+dx[i]
            nj = y+dy[i]
            if 0<=ni<n and 0<=nj<n and grid[ni][nj]==1:
                cnt+=1
        if cnt>=3:
            result+=1
print(result)