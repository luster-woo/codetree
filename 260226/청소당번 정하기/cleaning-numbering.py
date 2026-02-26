n = int(input())
a,b,c=0,0,0
for x in range(1,n+1):
    if x%12==0:
        c+=1
    elif x%3==0:
        b+=1
    elif x%2==0:
        a+=1
print(a,b,c)