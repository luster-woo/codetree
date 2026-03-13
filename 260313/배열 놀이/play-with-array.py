import sys

# 입력을 빠르게 받기 위한 설정
input = sys.stdin.readline

n, q = map(int, input().split())
arr = list(map(int, input().split()))

# 2번 쿼리(값 찾기)를 위해 위치(index)를 미리 저장해두는 전략
# {값: 인덱스+1} 형태의 딕셔너리 생성
pos_dict = {}
for i in range(n):
    # 만약 중복 값이 있다면 마지막 인덱스가 저장됨 (문제 조건 확인 필요)
    pos_dict[arr[i]] = i + 1

for _ in range(q):
    temp = list(map(int, input().split()))
    if not temp: continue # 빈 줄 방지
    
    query_type = temp[0]
    
    if query_type == 1:
        # 인덱스 범위 체크를 추가하면 더 안전함
        idx = temp[1] - 1
        if 0 <= idx < n:
            print(arr[idx])
            
    elif query_type == 2:
        # in arr나 .index() 대신 딕셔너리 검색 (매우 빠름)
        # 딕셔너리에 없으면 0 출력
        print(pos_dict.get(temp[1], 0))
            
    elif query_type == 3:
        # 슬라이싱 범위를 안전하게 잡기
        start, end = temp[1] - 1, temp[2]
        print(*(arr[start:end]))