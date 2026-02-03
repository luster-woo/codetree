def calculrator(a, o, c):
    if o not in "+-/*":
        return False
    if o == "+":
        return f'{a} {o} {c} = {a+c}'
    elif o == "-":
        return f'{a} {o} {c} = {a-c}'
    elif o == "/":
        return f'{a} {o} {c} = {a//c}'
    else:
        return f'{a} {o} {c} = {a*c}'

a, o, c = input().split()
a = int(a)
c = int(c)
print(calculrator(a, o, c))
