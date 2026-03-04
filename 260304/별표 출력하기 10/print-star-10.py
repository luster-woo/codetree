n = int(input())

arr = []

# 앞 절반 만들기
for i in range(n):
    if i % 2 == 0:
        arr.append(i//2 + 1)
    else:
        arr.append(n - i//2)

# 전체 패턴 = 앞 + 앞을 거꾸로
pattern = arr + arr[::-1]

# 출력
for num in pattern:
    print("* " * num)