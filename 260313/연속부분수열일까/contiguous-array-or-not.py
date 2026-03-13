n,m = map(int,input().split())
arr =list(map(int,input().split()))
temp =list(map(int,input().split()))
i=j=0
result = "No"
while i<n-m:
    if arr[i:i+m]==temp:
        result="Yes"
        break
    i+=1
print(result)
    