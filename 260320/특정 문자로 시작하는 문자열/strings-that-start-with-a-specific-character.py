n = int(input())
arr = []
cnt = 0
for _ in range(n):
    temp = input()
    arr.append(temp)
a = input()
result = 0
for x in arr:
    if x[0]==a:
        cnt+=1
        result+=len(x)
print(f'{cnt} {result/cnt:0.2f}')
