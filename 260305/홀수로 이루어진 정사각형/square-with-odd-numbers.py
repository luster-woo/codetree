import sys

def solve():
    # 정수 N 입력 받기
    try:
        line = sys.stdin.readline()
        if not line:
            return
        n = int(line.strip())
    except ValueError:
        return

    # N x N 루프 돌며 숫자 계산
    for i in range(n):      # i는 행(row)
        row_list = []
        for j in range(n):  # j는 열(column)
            # 기본 시작값 11에 (i + j)만큼의 홀수 간격(2씩)을 더함
            num = 11 + (i + j) * 2
            row_list.append(str(num))
        
        # 한 줄씩 출력
        print(" ".join(row_list))

if __name__ == "__main__":
    solve()