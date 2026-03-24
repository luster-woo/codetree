s = input()
result = ''

for x in s:
    if x.isupper():
        result += x.lower()
    elif x.islower():
        result += x.upper()

print(result)