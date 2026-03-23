a = list(input())
b = input()
i = 0
while i<len(a):
    cnt = 0
    if ''.join(a[i:i+len(b)])==b:
        while cnt !=len(b):
            a.pop(i)
            cnt+=1
        i = 0
    else:
        i+=1
print(''.join(a))
