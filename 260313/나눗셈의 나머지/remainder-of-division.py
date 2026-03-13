a, b = map(int, input().split())
count = [0] * b

while a > 1:
    count[a % b] += 1
    a //= b

print(sum(c*c for c in count))