import math
arr = list(map(int,input().split()))
temp = 0
temp_1 = 0
for x in range(10):
    if x%2==0:
        temp+=arr[x]
    else:
        temp_1 +=arr[x]
print(abs(temp-temp_1))