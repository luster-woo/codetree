a = input()
b = input()
result = ''
result_1 = ''
for x in a:
    if x.isdigit():
        result+=x
for x in b:
    if x.isdigit():
        result_1+=x
        
result = int(result)
result_1 = int(result_1)
print(result+result_1)
                