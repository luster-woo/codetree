dirs = input()
dx = [0,1,0,-1]
dy = [1,0,-1,0]
i = 2
for x in dirs:
    if x=="L":
        i = (i+1)%4
    elif x=="R":
        i = (i-1)%4
    else:
        print(dx[i],dy[i])
# Please write your code here.