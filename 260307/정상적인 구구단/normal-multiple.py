n = int(input())
for x in range(1,n+1):
    for y in range(1,n+1):
        if y == n:
            print(f'{x} * {y} = {x*y}')
        else:           
            print(f'{x} * {y} = {x*y},',end=" ")
        