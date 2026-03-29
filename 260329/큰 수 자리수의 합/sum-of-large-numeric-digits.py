def digit_sum(n):
    # 종료 조건
    if n == 0:
        return 0
    
    # 재귀
    return (n % 10) + digit_sum(n // 10)


a, b, c = map(int, input().split())

result = a * b * c

print(digit_sum(result))