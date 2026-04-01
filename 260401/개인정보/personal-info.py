n = 5
person = []

for _ in range(n):
    n, h, w = input().split()
    person.append((n,int(h),float(w)))
print("name")
person.sort(key = lambda x : x[0])
for n,h,w in person:
    print(n,h,w)
print()
print("height")
person.sort(key = lambda x : -x[1])
for n,h,w in person:
    print(n,h,w)