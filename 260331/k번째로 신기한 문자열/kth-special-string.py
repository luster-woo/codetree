n,k,ans = map(str,input().split())
n = int(n)
k = int(k)
arr = []
length = len(ans)
for _ in range(n):
    temp = input()
    if temp[:length]==ans:
        arr.append(temp)
arr.sort()
print(arr[k-1])