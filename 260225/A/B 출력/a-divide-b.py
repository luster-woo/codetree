a, b = map(int, input().split())

# 정수 부분 출력
print(a // b, end=".")

# 나머지 부분으로 소수점 20자리까지 계산
rem = a % b
for _ in range(20):
    rem *= 10
    print(rem // b, end="")
    rem %= b