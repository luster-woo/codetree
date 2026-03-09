n = int(input())
a = 65
for x in range(1,n+1):
    for y in range(x):
        if a<=97:
            print(chr(a),end="")
        a+=1
        else:
            a=65:
            print(chr(a),end="")
        a+=1
    print()