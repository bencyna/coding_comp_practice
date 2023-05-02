test_cases = int(input())
while test_cases > 0:
    test_cases -=1
    n = int(input())
    nums = list(map(int, input().split()))

    if n == 1:
        print(-1)
        continue
    # sort the numbers
    sorted_nums = sorted(nums)
    i = 0
    while i < n:
        if sorted_nums[i] != nums[i]:
            # number is in its best position, leave it
            i+=1
            continue

        # number must be swapped with its next number, unless it is the last number
        if i != n-1:
            sorted_nums[i], sorted_nums[i+1] =  sorted_nums[i+1], sorted_nums[i]
            i+=2
        else:
            # swap it with previous, only in wrong positon if previous is ok to swap
            sorted_nums[i], sorted_nums[i-1] =  sorted_nums[i-1], sorted_nums[i]
    
    # print nums in order
    for i, num in enumerate(sorted_nums):
        if i == n-1:
            print(num)
        else:
            print(num, end=" ")

