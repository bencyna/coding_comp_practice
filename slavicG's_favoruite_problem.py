testCases = int(input())
while testCases > 0:
    testCases -= 1
    vertices, start, end = list(map(int, input().split()))
    start -= 1
    end -= 1
    # create adjList
    adjList = [[] for _ in range(vertices)]
    for i in range(vertices):
        # add edge and weight to both 
        u, v, w = list(map(int, input().split()))
        adjList[u-1].append([v-1, w])
        adjList[v-1].append([u-1, w])
        
    # we just need to see if theres a way to get to b from anywhere 