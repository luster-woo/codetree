m, D = map(int, input().split())

if m == 1 or m ==3 or m==5 or m==7 or m==8 or m==10 or m==12:
    if D>0 and D<=31:
        print("Yes")
    else:
        print("No")
elif m==4 or m==6 or m==9 or m==11:
    if D>0 and D<=30:
        print("Yes")
    else:
        print("No")  
else:
    if D>0 and D<=28:
        print("Yes")
    else:
        print("No") 