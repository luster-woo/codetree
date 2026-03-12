
arr = list(map(int, input().split()))

for i in range(100, 9,-10):
    cnt = 0
    for x in arr:
        if x == 0:
            break
        
        if x >= 10:

            if (x // 10)*10 == i:
                cnt += 1
                
    print(f"{i} - {cnt}")