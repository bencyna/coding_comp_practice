numOfTests = int(input().strip())

while numOfTests > 0:
    space = input()
    numOfTests -= 1

    length, numOfAirCons = list(map(int, input().split()))

    airCons = input().split()
    temperatures = input().split()
    airConVals = [[] for _ in range(numOfAirCons)]
    # pair aircons and temps and sort by values
    for i in range(numOfAirCons):
        airConVals[i] = (int(airCons[i])-1, int(temperatures[i]))
    
    airConVals.sort()
    # each distance away an aircon is, the temperature increases from that aircon by 1
    # find the min temperature for each cell
    res = [10**10] * length
    k = 0
    while k <= airConVals[0][0]:
        res[k] = airConVals[0][1]+airConVals[0][0]-k
        k+=1
    
    currentAirConIndex = 0
    # start from the left temp, make the temperature the min possible from the left + 1
    for i in range(k, length):
        res[i] = res[i-1]+1

        # check we haven't passed the last aircon
        if i <= airConVals[-1][0]:
            # check if we are up to the next aircon
            if i == airConVals[currentAirConIndex+1][0]:
                # we are at a new aircon
                currentAirConIndex += 1
                res[i] = min(res[i], airConVals[currentAirConIndex][1]) 
                
    # go through from the back, make the temp min at each point
    for i in range(length-2, -1, -1):
        res[i] = min(res[i], res[i+1]+1)
        
        # check we haven't reached past the first aircon
        if i >= airConVals[0][0]:
            if i == airConVals[currentAirConIndex-1][0]:
                currentAirConIndex -= 1
                res[i] = min(res[i], airConVals[currentAirConIndex][1]) 

    for result in res:
        print(result, end =" ")
    print("")