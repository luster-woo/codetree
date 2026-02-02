a, b = map(int, input().split())
list_1=[]
for i in range(a,b+1):
    cnt = 0
    for j in range(1,i+1):
        if i%j==0:
            cnt+=1
    if cnt==2:
        list_1.append(i)
print(sum(list_1))
    