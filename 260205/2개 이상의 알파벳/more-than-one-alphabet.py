A = input()
dic = {}
for ch in A:
    if ch in dic:
        dic[ch] += 1
    else:
        dic[ch] = 1

if len(dic)>=2:
    print("Yes")
else:
    print("No")
