a, b = map(int, input().split())
count = [0] * b
while a > 0:
    count[a % b] += 1
    a //= b
result = 0
for i in range(b):
    if count[i] != 0:
        result += count[i] ** 2
print(result)