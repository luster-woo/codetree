arr = list(map(int,input().split()))
temp = arr[1]+arr[3]+arr[5]+arr[7]+arr[9]
temp_1 = arr[2]+arr[5]+arr[8]
print(f'{temp} {temp_1//3:0.1f}')