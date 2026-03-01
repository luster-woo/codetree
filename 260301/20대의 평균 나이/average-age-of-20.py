cnt = 0
result = 0
while True:
    a = int(input())
    if a>=30:
        print(f'{result/cnt:0.2f}')
        break    
    cnt+=1
    result+=a