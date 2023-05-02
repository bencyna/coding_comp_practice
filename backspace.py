import collections
numOfTests = int(input().strip())

while numOfTests > 0:
    numOfTests -= 1
    s = list(input())
    t = list(input())
    
    if len(t) > len(s):
        print("no")
        continue
    
    if len(t) == 0:
        print("yes")
        continue    
    # get letter counts for both
    t_letters = set(t)
    t_idx = 0
    stack = []
    letterCount = 0
    found = False

    # for each letter in s
    # if current letter != t_index, we have to delete the current letter
    for s_idx, char in enumerate(s):
        # if current char is correct
        if char == t[t_idx]:
            # two options
            # prev is valid
            if not stack or stack[-1][1]:
                letterCount += 1
                stack.append([char, True])
                t_idx += 1
            else:
                # prev is deletable, we must skip current
                stack.pop()
                
                
        else:
            # current char is not the next item in our t string
            # either press backspace and pop or add to stack
            if stack and not stack[-1][1]:
                # remove last 
                stack.pop()
            elif stack:
                stack.append([char, False])
            # else the stack is empty continue don't add cur
        if letterCount == len(t):
            found = True
            break
    
    if found:
        print("Yes")      
    else:
        print("No")
    
    
     
hhsjjello
hello

aabada
abada