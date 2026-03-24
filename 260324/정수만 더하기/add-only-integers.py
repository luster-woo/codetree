arr = input()
result = 0
for x in arr:

    if x.isdigit():
        x = int(x)
        result+=x
print(result)