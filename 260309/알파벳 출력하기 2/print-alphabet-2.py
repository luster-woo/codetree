n = int(input())
a = 65
for x in range(n):
    print("  "*x,end="")
    for y in range(n-x):
        if a<91:
            print(chr(a),end=" ")
            a+=1
        else:
            a=65
            print(chr(a),end=" ")
            a+=1
    print()