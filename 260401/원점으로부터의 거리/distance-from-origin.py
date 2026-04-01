n = int(input())
dot = []
for x in range(n):
    a,b  = map(int,input().split())
    dot.append((abs(a)+abs(b),x))
dot.sort(key = lambda x : ((x[0],x[1])))
for a,b in dot:
    print(b+1)
# Please write your code here.