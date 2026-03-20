cnt = 0 
arr = []
for _ in range(10):
    temp = input()
    arr.append(temp)
a = input()
flag = False
for x in arr:
    if x[len(x)-1]==a:
        flag = True
        print(x)
if not flag:
    print("None")