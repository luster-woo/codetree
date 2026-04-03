k = int(input())
arr = [0]*100
for _ in range(k):
    a,b = map(int,input().split())
    for x in range(a-1,b):
        arr[x]+=1
print(max(arr))