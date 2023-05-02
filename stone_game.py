import math
test_cases = int(input().strip())
while test_cases > 0:
    test_cases -= 1
    
    num_stones = int(input().strip())
    
    nums = list(map(int, input().split()))
    
    # dp problem 
    # at each point we either take from the left or right
    # return once both min and max have been removed
    
    
    # first calulcate the min and max numbers 
    minVal = nums[0]
    maxVal = nums[0]
    
    #### maybe issue with str? ####
    for num in nums:
        minVal = min(minVal, num)
        maxVal = max(maxVal, num)
    
    # set up dp top down solution 
    cache = {}
    def dp(l, r, nums, foundMin, foundMax, minVal, maxVal, cache):
        # base case, l > r, return 0
        if foundMin and foundMax:
            return 0
        
        if l > r:
            # shoudln't happen
            return 10**10
        
        if (l, r) not in cache:
            # if l == minVal or maxVal 
            # return dp l+1 + 1
            foundLeftMin = foundMin or nums[l] == minVal       
            foundLeftMax = foundMax or nums[l] == maxVal            
            foundRightMin = foundMin or nums[r] == minVal            
            foundRightMax = foundMax or nums[r] == maxVal 
            
            cache[l, r] = min(dp(l+1, r, nums, foundLeftMin, foundLeftMax, minVal, maxVal, cache), dp(l, r-1, nums, foundRightMin, foundRightMax, minVal, maxVal, cache)) + 1               

        return cache[l,r]
    
    print(dp(0, len(nums)-1, nums, False, False, minVal, maxVal, cache))
    
    