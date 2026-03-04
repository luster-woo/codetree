n = int(input())

for i in range(1, n+1):
    if i % 2 == 1:   # 홀수 줄
        print("*")
    else:            # 짝수 줄
        print("* " * i)