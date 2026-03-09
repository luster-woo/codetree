s, e = map(int, input().split())
result = 0
for x in range(s,e+1):
    cnt = 0
    cnt_1=0
    for y in range(1,x+1):
        if x==y*y:
            cnt+=1
        elif x%y==0:
            cnt_1+=1
    if cnt ==1 and cnt_1==2:
        result+=1
print(result)