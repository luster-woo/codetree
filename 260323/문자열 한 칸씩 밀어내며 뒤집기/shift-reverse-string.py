import sys

input = sys.stdin.readline

data = input().split()
s = data[0]
q = int(data[1])

for _ in range(q):
    cmd = int(input())
    
    if cmd == 1:
        s = s[1:] + s[0]
        print(s)
    elif cmd == 2:
        s = s[-1] + s[:-1]
        print(s)
    elif cmd == 3:
        s = s[::-1]
        print(s)