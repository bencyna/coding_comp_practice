import collections
# n = number of users
# m number of friend groups

# for each m we're given
# 1 number of people in group, friends in group 

# for each player, show the number of people who would learn the news 
def bfs(node, adjList, seen, res):
    q = collections.deque([node])
    miniSeen = set()
    while q:
        node = q.popleft()
        miniSeen.add(node)
        # look for conencted nodes
        for nextNode in adjList[node]:
            # add to q if not in mini seen
            if nextNode not in miniSeen:
                q.append(nextNode)
    # go through seen and set their res
    nodeCount = len(miniSeen)
    for node in miniSeen:
        seen[node] = nodeCount
        res[node-1] = nodeCount
        
# create adjList  
n, m = list(map(int, input().split()))
adjList = [set() for _ in range(n+1)]
while m > 0:
    # create the adjLists
    m -= 1
    friends = list(map(int, input().split()))
    if friends[0] == 0:
        continue
    friend1 = friends[1]
    for i in range(2, friends[0]+1):
        friend2=friends[i]
        adjList[friend1].add(friend2)
        adjList[friend2].add(friend1)


seen = {}
res = [0 for _ in range(n)]
# traverse from each friend to all friends
for node in range(1, n+1):
    # if friend has been seen, we can just use that as the value
    if node in seen:
        res[node-1] = seen[node]
    else:
        # bfs
        bfs(node, adjList, seen, res)
    
for i in range(n):
    print(res[i], end=" ")
 
                
