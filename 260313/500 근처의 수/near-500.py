arr = list(map(int,input().split()))
val_1 = 0
val_2 = 10**9
for x in arr:
    if x<500 and x>val_1:
        val_1 = x
    elif x>500 and x<val_2:
        val_2 = x
print(val_1, val_2)