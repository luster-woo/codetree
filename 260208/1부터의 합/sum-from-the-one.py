num = int(input())
result = 0
for i in range(1,101):
    result += i
    if result >= num:   
        print(i)
        break
