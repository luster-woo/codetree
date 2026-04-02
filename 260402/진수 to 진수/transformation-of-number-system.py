A, B = map(int, input().split())
N = input().strip()

# 1. A진수 → 10진수
decimal = int(N, A)

# 2. 10진수 → B진수
def to_base(n, base):
    if n == 0:
        return "0"
    
    result = ""
    while n > 0:
        result += str(n % base)
        n //= base
    
    return result[::-1]

print(to_base(decimal, B))