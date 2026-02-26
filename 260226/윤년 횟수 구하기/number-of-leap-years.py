n = int(input())
cnt = 0 
for x in range(1,n+1):
    if x%4==0 and (x%100 !=0 or x%400==0):
        cnt+=1
print(cnt)