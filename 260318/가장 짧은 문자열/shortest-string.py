min_val = 10**9
max_val = 0
for _ in range(3):
    temp = input()
    min_val = min(min_val, len(temp))
    max_val = max(max_val, len(temp))
print(max_vla - min_val)