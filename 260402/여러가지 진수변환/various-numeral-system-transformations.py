N, B = map(int, input().split())

result = ""

# N이 0일 경우 처리
if N == 0:
    print(0)
else:
    while N > 0:
        result += str(N % B)
        N //= B

    print(result[::-1])