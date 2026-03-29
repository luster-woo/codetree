def sequence(n):
    # 종료 조건
    if n == 1:
        return 2
    if n == 2:
        return 4
    
    # 재귀
    return (sequence(n-1) * sequence(n-2)) % 100


N = int(input())
print(sequence(N))