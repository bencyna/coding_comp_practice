n = int(input())

nums = list(map(int, input().split()))

maxSubArr = 1
curSubArr = 1
for i in range(1, n):
    if nums[i-1] < nums[i]:
        curSubArr += 1
    else:
        curSubArr = 1
    maxSubArr = max(maxSubArr, curSubArr)

print(maxSubArr) 