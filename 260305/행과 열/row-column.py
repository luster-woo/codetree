n,m = map(int,input().split())
maze=[[0]*m for _ in range(n)]
for x in range(n):
    for y in range(m):
        maze[x][y] = (x+1)*(y+1)
for x in range(n):
    for y in range(m):
        print(maze[x][y],end=" ")
    print()