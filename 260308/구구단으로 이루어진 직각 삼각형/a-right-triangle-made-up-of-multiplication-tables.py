n = int(input())

for i in range(1, n + 1):
    # 각 행에서 출력할 식들을 담을 리스트
    row_items = []
    
    # 곱해지는 숫자의 개수는 (n - i + 1)개
    for j in range(1, n - i + 2):
        row_items.append(f"{i} * {j} = {i * j}")
    
    # 리스트 요소들 사이에 ' / '를 넣어서 출력
    print(" / ".join(row_items))