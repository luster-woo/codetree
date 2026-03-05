n = int(input())
cnt = 2
maze = [[0]*n for _ in range(n)]
for x in range(n):
    for y in range(n):
        if cnt>9:
            cnt=2
        maze[x][y]=cnt
        cnt+=2
for x in range(n):
    for y in range(n):
        print(maze[x][y],end=" ")
    print()
