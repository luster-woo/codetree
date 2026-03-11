n = int(input())
arr = list(map(int,input().split()))
temp = [x**2 for x in arr]
print(*temp)