class Person:
    def __init__(self, name, address, region):
        self.name = name
        self.address = address
        self.region = region


n = int(input())
people = []

# 입력
for _ in range(n):
    name, address, region = input().split()
    people.append(Person(name, address, region))

# 사전순 가장 느린 사람 찾기 (가장 큰 이름)
target = people[0]
for p in people:
    if p.name > target.name:
        target = p

# 출력
print(f"name {target.name}")
print(f"addr {target.address}")
print(f"city {target.region}")