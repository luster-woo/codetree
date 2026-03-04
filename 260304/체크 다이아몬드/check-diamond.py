n = int(input())

# 전체 줄 수 = 2n - 1
for i in range(1, 2*n):
    if i <= n:
        star = i
    else:
        star = 2*n - i
    
    print(" " * (n - star) + "* " * star)