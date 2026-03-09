
arr = list(map(int,input().split()))
idx = 0
for x in arr:
    if x >=250:
        idx = arr.index(x)
        break
result = sum(arr[:idx])
print(f'{result} {result/idx:0.1f}')