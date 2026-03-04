n = int(input())

arr = []

# 앞 절반 만들기
for i in range(n):
    if i % 2 == 0:        # 짝수 인덱스
        arr.append(n - i//2)
    else:                 # 홀수 인덱스
        arr.append(i//2 + 1)

# 전체 패턴 = 앞 + 뒤(뒤집기)
pattern = arr + arr[::-1]

# 출력
for num in pattern:
    print("* " * num)