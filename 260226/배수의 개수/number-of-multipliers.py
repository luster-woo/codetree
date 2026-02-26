cnt_a = 0 
cnt_b = 0
for _ in range(10):
    a = int(input())
    if a%3==0:
        cnt_a +=1
    if a%5==0:
        cnt_b +=1
print(cnt_a, cnt_b)