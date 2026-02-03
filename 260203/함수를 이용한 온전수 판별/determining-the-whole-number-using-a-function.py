def num(i):
    if i%2!=0 and i%10!=5 and (i % 3 != 0 or i % 9 == 0):
        return 1
    else:
        return 0
a, b = map(int, input().split())
result = 0
for i in range(a,b+1):
    c = num(i)
    result+=c
print(result)