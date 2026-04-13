
n,k,p,t = map(int,input().split())
arr = []
for _ in range(t):
    t, x, y = map(int, input().split())
    arr.append((t, x, y))
arr.sort(key = lambda x : x[0])
people = [k]*n
result = [0]*n
result[p-1]=1
for _,x,y in arr:
    if people[x-1]>0 and result[x-1]==1:
        result[y-1]=1
        people[x-1]-=1
    if people[y-1]>0 and result[y-1]==1:
        people[y-1]-=1
        result[x-1]=1
for x in range(n):
    print(result[x],end="")