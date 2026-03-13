n = int(input())
price = list(map(int, input().split()))
max_val = 0
# Please write your code here.
for x in range(n):
    for y in range(x,n):
        if price[y]-price[x]>max_val:
            max_val = price[y]-price[x]
print(max_val)