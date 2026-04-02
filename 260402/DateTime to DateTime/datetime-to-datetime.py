a, b, c = map(int, input().split())
result = 11*24*60+11*60+11
temp  = a*24*60+b*60+c
if temp>=result:
    print(temp-result)
else:
    print(-1)
# Please write your code here.