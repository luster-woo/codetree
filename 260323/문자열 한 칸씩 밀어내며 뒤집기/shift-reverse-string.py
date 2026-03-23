import sys

s = sys.stdin.readline().strip()
q = int(sys.stdin.readline())

for _ in range(q):
    cmd = int(sys.stdin.readline())
    
    if cmd == 1:
        s = s[1:] + s[0]
        print(s)
    elif cmd == 2:
        s = s[-1] + s[:-1]
        print(s)
    elif cmd == 3:
        s = s[::-1]
        print(s)