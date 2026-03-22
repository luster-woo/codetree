arr = list(input())
temp = arr[0]
temp_1 = arr[1]
result = ''
for x in arr:
    if x == temp:
        result+=temp_1
    elif x ==temp_1:
        result+=temp
    else:
        result+=x
print(''.join(result))