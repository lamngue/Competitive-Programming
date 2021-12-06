def notOutOfBound(x, y, r, c):
    return x >= 0 and y >= 0 and x < c and y < r

def DFS(start, end, graph):
    s = []
    s.append(start)
    curX = start[0]
    curY = start[1]
    flag = False
    cost[curY][curX] = 0
    visited[curY][curX] = True
    while len(s) > 0:
        u = s.pop()
        #if found the exit
        if (u[0] == end[0] and u[1] == end[1]):
            print(cost[u[1]][u[0]])
            flag = True
            break
        #moveUp
        curX = u[0]
        curY = u[1] + 1
        if (notOutOfBound(curX, curY, r, c) and
            graph[curY][curX] == '' and not visited[curY][curX]):
            cost[curY][curX] = cost[u[1]][u[0]] + 1
            visited[curY][curX] = True
            s.append((curX, curY))
        #move down
        curY = u[1] - 1
        if (notOutOfBound(curX,curY, r, c) and
            graph[curY][curX] == '' and not visited[curY][curX]):
            cost[curY][curX] = cost[u[1]][u[0]] + 1
            visited[curY][curX] = True
            s.append((curX, curY))
        #move left
        curX = u[0] - 1
        curY = u[1]
        if (notOutOfBound(curX,curY, r, c) and
            graph[curY][curX] == '' and not visited[curY][curX]):
            cost[curY][curX] = cost[u[1]][u[0]] + 1
            visited[curY][curX] = True
            s.append((curX, curY))
        #move right
        curX = u[0] + 1
        curY = u[1]
        if (notOutOfBound(curX,curY, r, c) and
            graph[curY][curX] == '' and not visited[curY][curX]):
            cost[curY][curX] = cost[u[1]][u[0]] + 1
            visited[curY][curX] = True
            s.append((curX, curY))
        if (flag):
            break
        
while True:
    r, c = map(int, input().split())
    if (r == 0 and c == 0):
        break
    graph = [['' for i in range(c)] for i in range(r)]
    visited = [[False for i in range(c)] for i in range(r)]
    cost = [[None for i in range(c)] for i in range(r)]
    startX = 0
    startY = 0
    R = int(input())
    for i in range(R):
        line = list(map(int, input().split()))
        rowNo = line[0]
        b = line[1]
        for j in range(2, len(line)):
            graph[rowNo][line[j]] = 'bomb'
    startY, startX = map(int, input().split())
    endY, endX = map(int, input().split())
    start = (startX, startY)
    end = (endX, endY)
    DFS(start, end, graph)
