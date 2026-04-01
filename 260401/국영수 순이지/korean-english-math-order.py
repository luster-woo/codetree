n = int(input())
people = [ ]
for _ in range(n):
    n_i, h_i, w_i,a_i = input().split()
    people.append((n_i,int(h_i),int(w_i),int(a_i)))
people.sort(key=lambda x: (-x[1], -x[2], -x[3]))
for name, height, weight,a in people:
    print(name, height, weight,a)