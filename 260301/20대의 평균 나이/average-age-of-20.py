cnt = 0
total = 0

while True:
    a = int(input())
    
    if 20 <= a < 30:
        cnt += 1
        total += a
    else:
        break

print(f"{total/cnt:.2f}")