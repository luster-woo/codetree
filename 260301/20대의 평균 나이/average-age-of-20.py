cnt = 0
result = 0

while True:
    a = int(input())
    if a >= 30:
        if cnt == 0:
            print("0.00")
        else:
            print(f'{result/cnt:0.2f}')
        break
    cnt += 1
    result += a