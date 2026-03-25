A = input().strip()
B = input().strip()

n = len(A)

for k in range(1, n + 1):
    rotated = A[-k:] + A[:-k]
    if rotated == B:
        print(k)
        break
else:
    print(-1)