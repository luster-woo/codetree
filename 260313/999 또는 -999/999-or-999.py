max_val = -1000
min_val = 1000
count = 0

while count < 100:
    # 한 줄씩 입력받음 (데이터가 줄 단위로 들어온다고 가정)
    line = input().split()
    if not line: break # 더 이상 입력이 없으면 종료
    
    stop = False
    for char in line:
        val = int(char)
        if val == 999 or val == -999:
            stop = True
            break
        
        # 값 업데이트
        if val > max_val: max_val = val
        if val < min_val: min_val = val
        
        count += 1
        if count >= 100:
            stop = True
            break
            
    if stop: break

print(max_val, min_val)