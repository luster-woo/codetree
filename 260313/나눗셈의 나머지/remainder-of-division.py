a, b = map(int, input().split())
count = [0] * b

while True:
    count[a % b] += 1
    a //= b
    if a == 0:
        break

print(sum(c*c for c in count))