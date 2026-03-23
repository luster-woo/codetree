import sys

input = sys.stdin.readline

s = input().strip()
commands = input().strip()

for cmd in commands:
    if cmd == 'L':
        s = s[1:] + s[0]
    elif cmd == 'R':
        s = s[-1] + s[:-1]

print(s)