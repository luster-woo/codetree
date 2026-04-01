class User:
    def __init__(self, id, level):
        self.id = id
        self.level = level

u1 = User("codetree", 10)

id2, level2 = input().split()
u2 = User(id2, int(level2))

print(f"user {u1.id} lv {u1.level}")
print(f"user {u2.id} lv {u2.level}")