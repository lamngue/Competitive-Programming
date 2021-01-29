import queue
t = int(input())

def notOutOfBound(x, y, m, n):
    return x >= 0 and y >= 0 and x < n and y < m

def checkInAndOut(graph, m, n):
    #exactly 2 openings in the edges)
    points = []
    openings = 0
    for i in range(n):
        if (graph[0][i] == '.'):
            points.append((i, 0))
            openings += 1
    if (m > 1): #more than 1 row
        for i in range(n):
            if (graph[m-1][i] == '.'):
                points.append((i, m-1))
                openings += 1
    for j in range(1,m-1):
        if (graph[j][0] == '.'):
            points.append((0, j))
            openings += 1
    if (n > 1): #more than 1 column
        for j in range(1,m-1):
            if (graph[j][n-1] == '.'):
                points.append((n-1, j))
                openings += 1
    return points

def BFS(start, end, graph, visited, n, m):
    q = queue.Queue()
    q.put(start)
    curX = start[0]
    curY = start[1]
    visited[curY][curX] = True
    while not q.empty():
        u = q.get()
        #if found the exit
        if (u[0] == end[0] and u[1] == end[1]):
            return True
        #moveUp
        curX = u[0]
        curY = u[1] + 1
        if (notOutOfBound(curX, curY, m, n) and
            graph[curY][curX] == '.' and not visited[curY][curX]):
            visited[curY][curX] = True
            q.put((curX, curY))
        #move down
        curY = u[1] - 1
        if (notOutOfBound(curX,curY, m, n) and
            graph[curY][curX] == '.' and not visited[curY][curX]):
            visited[curY][curX] = True
            q.put((curX, curY))
        #move left
        curX = u[0] - 1
        curY = u[1]
        if (notOutOfBound(curX,curY, m, n) and
            graph[curY][curX] == '.' and not visited[curY][curX]):
            visited[curY][curX] = True
            q.put((curX, curY))
        #move right
        curX = u[0] + 1
        curY = u[1]
        if (notOutOfBound(curX,curY, m, n) and
            graph[curY][curX] == '.' and not visited[curY][curX]):
            visited[curY][curX] = True
            q.put((curX, curY))
    return False
        
for i in range(t):
    m, n = map(int, input().split())
    graph = [['' for i in range(n)] for i in range(m)]
    visited = [[False for i in range(n)] for i in range(m)]
    for j in range(m):
        line = list(input())
        for k in range(n):
            graph[j][k] = line[k]

    points = checkInAndOut(graph, m, n)
    if (len(points) == 2):
        start = points[0]
        end = points[1]
        valid = BFS(start, end, graph, visited, n, m)
        if (valid):
            print("valid")
        else:
            print("invalid")
    else:
        print("invalid")
