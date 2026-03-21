arr = input()
n  = int(input())
cnt = 0
for x in arr[::-1]:
    print(x,end="")
    cnt+=1
    if cnt==n:
        break