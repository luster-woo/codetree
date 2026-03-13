a,b = map(int,input().split())
count = [0]*10
while True:
    if a//b==0:
        count[a%b]+=1
        break
    else:
        count[a%b]+=1
        a//=b
result = 0
for i in range(10):
    if count[i]!=0:
        result+=count[i]**2
print(result)