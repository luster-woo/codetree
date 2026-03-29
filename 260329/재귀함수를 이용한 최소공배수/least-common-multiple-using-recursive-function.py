def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def lcm(a, b):
    return a * b // gcd(a, b)

def recur(arr, n):
    if n == 1:
        return arr[0]
    return lcm(recur(arr, n-1), arr[n-1])


n = int(input())
arr = list(map(int, input().split()))

print(recur(arr, n))