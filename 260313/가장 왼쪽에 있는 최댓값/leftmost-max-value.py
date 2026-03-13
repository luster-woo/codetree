n = int(input())
a = list(map(int, input().split()))
max_val = max(a)
idx = a.index(max_val)+1
print(idx,end=" ")
a = a[:idx-1]
while idx>1:
    idx =a.index(max(a))+1
    print(idx,end=" ")
    a = a[:idx-1]
