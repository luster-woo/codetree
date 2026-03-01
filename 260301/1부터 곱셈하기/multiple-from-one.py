n = int(input())
result =1
for x in range(1,11):
    result*=x
    if result>=n:
        print(x)
        break
    