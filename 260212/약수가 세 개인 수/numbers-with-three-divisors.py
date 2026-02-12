start, end = map(int, input().split())
count = 0
for i in range(start,end+1):
    cnt = 0
    for j in range(1,i+1):
        if i%j==0:
            cnt+=1
    if cnt == 3:
        count+=1
print(count)
        
# Please write your code here.
