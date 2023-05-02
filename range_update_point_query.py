numberOfTestCases = int(input())

while numberOfTestCases >0: #O(T) (can;t do anything about this)
    sizeOfArr = input().split
    numberOfQueries = int(sizeOfArr[1])
    nums = list(map(int, input().split()))
    for _ in range(numberOfQueries):
        # two possibilities 
        q = list(map(int, input().split()))
        
        if q[0] == 1:
            l = q[1]-1
            r = q[2]
            
            # for each index i bwteen left and right, you should update the value of ai to the sum of its digits
            for k in range(l, r):
                temp = nums[k]
                sumOfDigits = 0
                while temp > 0:
                    sumOfDigits += temp % 10
                    temp//=10
                nums[k] = sumOfDigits
        
        else:
            x = q[1]-1
            print(nums[x])
            
    numberOfTestCases -= 1