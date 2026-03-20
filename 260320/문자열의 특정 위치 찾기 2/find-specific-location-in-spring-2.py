fruits = ["apple", "banana", "grape", "blueberry", "orange"]
a = input()
cnt = 0
for x in range(5):
    if a in fruits[x][2] or a in fruits[x][3]:
        print(fruits[x])
        cnt+=1
print(cnt)