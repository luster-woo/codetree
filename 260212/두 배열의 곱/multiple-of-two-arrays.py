arr = [list(map(int,input().split())) for _ in range(3)]
a= input()
arr_1 = [list(map(int,input().split())) for _ in range(3)]
for i in range(3):
    for j in range(3):
        print(arr[i][j]* arr_1[i][j],end = " ")
    print()