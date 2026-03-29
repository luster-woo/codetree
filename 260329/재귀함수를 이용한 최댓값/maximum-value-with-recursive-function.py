def find_max(arr, idx):
    # 종료 조건
    if idx == len(arr) - 1:
        return arr[idx]
    
    # 재귀 호출
    return max(arr[idx], find_max(arr, idx + 1))


N = int(input())
arr = list(map(int, input().split()))

print(find_max(arr, 0))