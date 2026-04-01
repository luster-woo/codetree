class Product:
    def __init__(self, name, code):
        self.name = name
        self.code = code


# 첫 번째 객체 (고정값)
p1 = Product("codetree", 50)

# 두 번째 객체 (입력)
name, code = input().split()
p2 = Product(name, int(code))

# 출력
print(f"product {p1.code} is {p1.name}")
print(f"product {p2.code} is {p2.name}")