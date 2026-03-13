n = int(input())
nums = list(map(int, input().split()))
nums.sort(reverse=True)
count = [0]*1000
for x in nums:
    count[x]+=1
cnt = max(nums)
max_val = -1
for i in range(1,cnt+1):
    if count[i]==1:
        max_val = i
print(max_val)