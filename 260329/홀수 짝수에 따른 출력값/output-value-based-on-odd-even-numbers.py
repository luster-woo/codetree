def recursive_sum(n):
    # 종료 조건
    if n == 1:
        return 1
    if n == 2:
        return 2
    
    # 재귀 호출
    return n + recursive_sum(n - 2)


N = int(input())

if N % 2 == 1:  # 홀수
    print(recursive_sum(N))
else:           # 짝수
    print(recursive_sum(N))