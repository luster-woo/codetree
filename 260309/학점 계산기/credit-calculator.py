n = int(input())
arr = list(map(float,input().split()))

score = sum(arr)/n

print(f'{score:.1f}')

if score >= 4:
    print("Perfect")
elif score >= 3:
    print("Good")
else:
    print("Poor")