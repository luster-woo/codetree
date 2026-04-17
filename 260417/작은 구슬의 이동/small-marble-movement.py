n, t = map(int, input().split())
r, c, d = input().split()
r, c = int(r), int(c)

dx = [0,1,0,-1]
dy = [1,0,-1,0]

# 🔥 처음에만 변환
if d == "R":
    i = 0
elif d == "D":
    i = 1
elif d == "L":
    i = 2
else:
    i = 3

while t > -1:
    ni = r + dx[i]
    nj = c + dy[i]
    if not (0 <= ni < n and 0 <= nj < n):
        i = (i + 2) % 4
        ni = r + dx[i]
        nj = c + dy[i]

    r = ni
    c = nj
    t -= 1

print(r, c)