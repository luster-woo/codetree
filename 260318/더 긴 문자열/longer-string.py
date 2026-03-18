a,b = map(str,input())
if len(a)>len(b):
    print(a,end=" ")
    print(len(a))
elif len(a)<len(b):
    print(b,end=" ")
    print(len(b))
else:
    print("sam")