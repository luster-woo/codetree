n = int(input())
a = list(map(int, input().split()))
print(f'{min(a)} {a.count(min(a))}')