cnt = 0
list = []
while True :
    temp  =input()
    if temp=="0":
        break
    else:
        cnt+=1
        list.append(temp)
print(cnt)
for x in range(len(list)):
    if x%2==0:
        print(list[x])