n = int(input())
people = []

for i in range(n):
    h, w = map(int, input().split())
    people.append((h, w, i + 1))  # (키, 몸무게, 번호)

# 정렬
people.sort(key=lambda x: (-x[0], -x[1], x[2]))


for h, w, idx in people:
    print(h,w,idx)