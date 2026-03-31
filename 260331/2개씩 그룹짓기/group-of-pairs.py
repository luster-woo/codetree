n = int(input())
arr = list(map(int, input().split()))

arr.sort()

answer = 0

for i in range(n):
    answer = max(answer, arr[i] + arr[2*n - 1 - i])

print(answer)