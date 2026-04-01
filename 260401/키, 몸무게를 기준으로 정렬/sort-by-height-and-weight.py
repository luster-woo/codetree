n = int(input())
person = []
for _ in range(n):
    n, h, w = input().split()
    person.append((n,int(h),int(w)))
person.sort(key = lambda x : (x[1],-x[2]))
for n,h,w in person:
    print(n,h,w)
# Please write your code here.