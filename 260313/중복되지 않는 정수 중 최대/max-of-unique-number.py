import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

# 1. 빈도수 체크 (O(N))
counts = {}
for x in nums:
    counts[x] = counts.get(x, 0) + 1

# 2. 내림차순 정렬 (O(N log N))
# 가장 큰 수부터 확인하기 위해 정렬된 키 값을 순회
sorted_keys = sorted(counts.keys(), reverse=True)

# 3. 빈도가 1인 가장 큰 수 찾기 (O(N))
max_val = -1
for x in sorted_keys:
    if counts[x] == 1:
        max_val = x
        break # 찾자마자 종료 (최적화 핵심)

print(max_val)