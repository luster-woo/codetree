s = input().strip()
n = len(s)

# 원래 문자열 한 번 출력
print(s)

# 한 칸씩 밀면서 n번 반복 (마지막에 자기 자신으로 돌아옴)
current = s
for _ in range(n):
    # 맨 뒤 글자 + 나머지 글자들 = 오른쪽으로 한 칸 회전
    current = current[-1] + current[:-1]
    print(current)