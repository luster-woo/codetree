a,b = map(str,input().split())
result = ''
result_1 = ''
for x in a:
    if x.isdigit():
        result+=x
    else:
        break
for x in b:
    if x.isdigit():
        result_1+=x
    else:
        break
result = int(result)
result_1 = int(result_1)
print(result+result_1)
                