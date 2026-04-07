n, T = map(int, input().split())
arr = list(map(int, input().split()))

max_val = 0
temp = 0

for x in arr:
    if x > T:
        temp += 1
        max_val = max(max_val, temp)
    else:
        temp = 0

print(max_val)