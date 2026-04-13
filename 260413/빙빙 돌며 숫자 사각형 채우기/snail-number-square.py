dx = [0,1,0,-1]
dy = [1,0,-1,0]
a,b = map(int,input().split())
arr = [[0]*b for _ in range(a)]
x,y =0,0
i = 0
for cnt in range(1,a*b+1):
    arr[x][y]=cnt
    ni = x+dx[i]
    nj = y+dy[i]
    if not(0<=ni<a) or not(0<=nj<b) or arr[ni][nj]!=0:
        i = (i+1)%4
    x +=dx[i]
    y+=dy[i]
for x in arr:
    print(*x)