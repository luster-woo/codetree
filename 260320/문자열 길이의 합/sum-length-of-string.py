result = 0
cnt = 0 
n = int(input())
for _ in range(n):
    arr = input()
    if arr[0]=="a":
        cnt+=1
    result+=len(arr)
print(result,cnt)