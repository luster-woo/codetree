a,b = map(str,input().split())
a = list(a)
b = list(b)
temp = a+b
temp_1 = b+a
temp =  ''.join(temp)
temp_1 =  ''.join(temp_1)
temp = int(temp)
temp_1 = int(temp_1)
print(temp+temp_1)