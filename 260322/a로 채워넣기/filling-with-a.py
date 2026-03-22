s = list(input())

if len(s) >= 2:
    s[1] = 'a'      # 앞에서 2번째
    s[-2] = 'a'     # 뒤에서 2번째

print(''.join(s))