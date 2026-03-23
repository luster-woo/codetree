arr =list(input())
arr.append(arr[0])
arr.pop(0)
print(''.join(arr))