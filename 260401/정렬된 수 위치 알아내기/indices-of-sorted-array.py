n = int(input())
arr = list(map(int, input().split()))

point = []
for i in range(n):
    point.append((arr[i], i))  # (값, 원래 인덱스)

# 값 기준 정렬, 값 같으면 원래 인덱스 기준
point.sort(key=lambda x: (x[0], x[1]))

ans = [0] * n

# 정렬된 위치를 기록
for new_idx, (value, old_idx) in enumerate(point):
    ans[old_idx] = new_idx + 1  # 1-based index

print(*ans)