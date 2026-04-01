class Bomb:
    def __init__(self, code, color, second):
        self.code = code
        self.color = color
        self.second = second


# 입력
code, color, second = input().split()

# 객체 생성
bomb = Bomb(code, color, int(second))

# 출력
print(f"code : {bomb.code}")
print(f"color : {bomb.color}")
print(f"second : {bomb.second}")