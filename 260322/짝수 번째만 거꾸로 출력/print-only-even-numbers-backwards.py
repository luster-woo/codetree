arr = list(input())
result = ''
for x in range(len(arr)):
    if x%2==1:
        result+=arr[x]
print(result[::-1])
