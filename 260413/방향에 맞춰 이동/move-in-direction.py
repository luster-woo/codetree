dx = [0,1,0,-1]
dy = [1,0,-1,0]
# Please write your code here.
n = int(input())
x,y=0,0
for _ in range(n):
    a,b = map(str,input().split())
    b = int(b)
    if a=="N":
        x+=dx[1]*b
        y+=dy[1]*b
    elif a=="E":
        x+=dx[0]*b
        y+=dy[0]*b
    elif a=="S":
        x+=dx[3]*b
        y+=dy[3]*b
    else:
        x+=dx[2]*b
        y+=dy[2]*b
    
print(y,x)