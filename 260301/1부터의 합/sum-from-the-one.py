result = 0
n = int(input())
for x in range(1,101):
    result+=x
    if result>=n:
        print(x)
        break