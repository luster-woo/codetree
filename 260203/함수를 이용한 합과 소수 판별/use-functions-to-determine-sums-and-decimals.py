def prime(num):
    if num < 2:
        return 0

    n = num % 10
    m = num // 10

    if (n + m) % 2 != 0:
        return 0

    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1

    if count == 2:
        return 1
    else:
        return 0


a, b = map(int, input().split())
result = 0

for i in range(a, b + 1):
    result += prime(i)

print(result)
