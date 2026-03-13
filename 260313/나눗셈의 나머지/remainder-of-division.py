a, b = map(int, input().split())
count = [0] * 10

# a가 0이 될 때까지 반복하며 b로 나눈 나머지를 구함
while a > 0:
    count[a % b] += 1
    a //= b

result = 0
for i in range(10):
    if count[i] != 0:
        result += count[i] ** 2
print(result)