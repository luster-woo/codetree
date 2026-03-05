n = int(input())
cnt = 1
maze = [[0]*n for _ in range(n)]
for x in range(n):
    for y in range(n):
        maze[x][y]=cnt
        cnt+=1
for x in range(n):
    for y in range(n):
        print(maze[x][y],end=" ")
    print()