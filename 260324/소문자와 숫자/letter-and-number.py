s = input()
result = ''

for x in s:
    if x.isalpha():
        result += x.lower()
    elif x.isdigit():
        result += x

print(result)