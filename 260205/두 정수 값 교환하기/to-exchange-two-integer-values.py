def change(a,b):
    return b,a


n, m = map(int, input().split())
result1, result2 = change(n,m)
print(result1,result2)
