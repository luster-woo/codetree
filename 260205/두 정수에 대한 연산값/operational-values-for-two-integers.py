def calcurator(a,b):
    if a<b:
        return a*2, b+25
    else:
        return a+25,b*2

a, b = map(int, input().split())
result_1,result_2 = calcurator(a,b)
print(result_1,resul)