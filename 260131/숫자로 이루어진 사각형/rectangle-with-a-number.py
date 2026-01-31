n = int(input())
count = 1
for i in range(n):
    for j in range(n):
        if count <= 9:
            print(count, end = " ")
            count +=1
        elif count == 10:
            count = 1
            print(count, end = " ")
            count +=1
    print()
# Please write your code here.