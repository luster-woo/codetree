for x in range(1,20):
    for y in range(1,20):
        if y%2!=0 and y<=18:
            print(f'{x} * {y} = {x*y} / ',end="")
        elif y%2==0:
            print(f'{x} * {y} = {x*y}')
        elif y==19:
            print(f'{x} * {y} = {x*y}')            
