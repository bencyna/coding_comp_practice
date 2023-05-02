s = input().strip()
prefixW = [0]*len(s)
postfixW = [0]*len(s)
j = len(s)-2
consecuitiveVsPre = s[0] == 'v'
consecuitiveVsPost = s[-1] == 'v'

# build prefix and suffix ws
for i in range(1, len(s)-1):
    postfix = s[j]
    prefix = s[i]    
    if prefix == "v":
        if consecuitiveVsPre:
            prefixW[i] = prefixW[i-1] +1
        else:
            prefixW[i] = prefixW[i-1] 
            
        consecuitiveVsPre = True
    else:
        prefixW[i] = prefixW[i-1] 
        consecuitiveVsPre = False

    if postfix == "v":
        if consecuitiveVsPost:
            postfixW[j] = postfixW[j+1] + 1
        else:    
            postfixW[j] = postfixW[j+1]
            
        consecuitiveVsPost = True
        
    else:
        postfixW[j] = postfixW[j+1] 
        consecuitiveVsPost = False

    j-=1

wow_factor = 0
for i in range(1, len(s)-1):
    if s[i] == "o":
        wow_factor += prefixW[i] * postfixW[i]

print(wow_factor)

