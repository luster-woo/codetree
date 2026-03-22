arr ,arr_1 = map(list,input().split())
result = arr[0:2]+arr_1[2:len(arr_1)]
print(''.join(result))