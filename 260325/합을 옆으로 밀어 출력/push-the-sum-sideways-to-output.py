n = int(input())
result  = 0
for _ in range(n):
    temp = int(input())
    result+=temp
result = list(str(result))
result.append(result[0])
result.pop(0)
print(''.join(result))