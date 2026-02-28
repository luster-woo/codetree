cnt = 0
result = 0
for _ in range(10):
    a = int(input())
    if 0<=a<=200:
        result+=a
        cnt+=1
print(f'{result} {result/cnt:0.1f}')