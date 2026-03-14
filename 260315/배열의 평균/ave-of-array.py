arr = [list(map(int,input().split())) for _ in range(2)]
for x in arr:
    print(f'{sum(x)/len(x):0.1f}',end=" ")
print()
temp = 0
result = 0
for i in range(4):
    for j in range(2):
        temp += arr[j][i]
        result +=arr[j][i]
    print(f'{temp/2:0.1f}',end=" ")
    temp = 0
print()
print(f'{result/8:0.1f}')
