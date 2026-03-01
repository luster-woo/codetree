while True:
    a = int(input())
    if a%2==1:
        continue
    else:
        print(a//2)
        a = int(input())
        if a%2==0:
            print(a//2)
        a = int(input())
        if a%2==0:
            print(a//2)
        a = int(input())
        if a%2==0:
            print(a//2)
        exit()