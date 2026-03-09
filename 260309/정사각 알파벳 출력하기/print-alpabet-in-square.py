n = int(input())
arr = [[0]*n for _ in range(n)]
a = 65
for x in range(n):
    for y in range(n):
        print(chr(a),end="")
        a+=1
    print()