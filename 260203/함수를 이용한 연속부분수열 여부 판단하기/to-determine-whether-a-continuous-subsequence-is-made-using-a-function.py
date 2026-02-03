def is_valid(a, b):
    for i in range(len(a) - len(b) + 1):
        if a[i:i+len(b)] == b:
            return "Yes"
    return "No"



n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

result = is_valid(a,b)
print(result)
# Please write your code here.