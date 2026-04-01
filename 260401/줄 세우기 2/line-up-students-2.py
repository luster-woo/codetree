n = int(input())

students = []
for i in range(n):
    h, w = map(int, input().split())
    students.append((h, w, i + 1))  # (키, 몸무게, 번호)

# 키 오름차순, 몸무게 내림차순
students.sort(key=lambda x: (x[0], -x[1]))

for h, w, idx in students:
    print(h, w, idx)