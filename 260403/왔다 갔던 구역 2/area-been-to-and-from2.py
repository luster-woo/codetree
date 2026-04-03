import sys
input = sys.stdin.readline
n = int(input())
arr = [0]*1000
start = 500
for _ in range(n):
    temp  = list(map(str,input().split()))
    if temp[1]=="R":
        for x in range(int(temp[0])):
            arr[start+x]+=1
        start+=int(temp[0])
    else:
        for x in range(int(temp[0])):
            arr[start-x]+=1
        start-=int(temp[0])
cnt = 0
for x in arr:
    if x>=2:
        cnt+=1
print(cnt)