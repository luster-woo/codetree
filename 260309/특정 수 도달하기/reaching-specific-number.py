
arr = list(map(int,input().split()))
idx = -1
for x in arr:
    if x >=250:
        idx = arr.index(x)
        break
if idx!=-1:
    result = sum(arr[:idx])
    print(f'{result} {result/idx:0.1f}')
else:
    result = sum(arr)
    print(f'{result} {result/10:0.1f}')