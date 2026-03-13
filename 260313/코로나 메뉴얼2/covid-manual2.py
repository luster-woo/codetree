a_cnt = 0
b_cnt = 0
c_cnt = 0
d_cnt = 0

for _ in range(3):
    a,b = input().split()
    if a=="Y" and int(b)>=37:
        a_cnt +=1
    elif a=="Y":
        c_cnt +=1
    elif a=="N" and int(b)>=37:
        b_cnt +=1
    else:
        d_cnt+=1
print(a_cnt,b_cnt,c_cnt,d_cnt,end=" ")
if a_cnt>=2:
    print("E")    