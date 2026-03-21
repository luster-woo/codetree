n = int(input())
arr = list(input().split())
result = ''.join(arr)

for i in range(0, len(result), 5):
    print(result[i:i+5])