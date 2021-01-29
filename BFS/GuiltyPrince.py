import queue
t = int(input())

def notOutOfBound(x, y, w, h):
    return x >= 0 and y >= 0 and x < w and y < h

def BFS(x, y, graph, visited, w, h):
    t = 1
    q = queue.Queue()
    q.put((x, y))
    while not q.empty():
        u = q.get()
        #move up
        curX = u[0]
        curY = u[1] + 1
        if (notOutOfBound(curX,curY, w, h) and
            graph[curY][curX] == '.' and not visited[curY][curX]):
            t += 1
            visited[curY][curX] = True
            q.put((curX, curY))
        #move down
        curY = u[1] - 1
        if (notOutOfBound(curX,curY, w, h) and
            graph[curY][curX] == '.' and not visited[curY][curX]):
            t += 1
            visited[curY][curX] = True
            q.put((curX, curY))
        #move left
        curX = u[0] - 1
        curY = u[1]
        if (notOutOfBound(curX,curY, w, h) and
            graph[curY][curX] == '.' and not visited[curY][curX]):
            t += 1
            visited[curY][curX] = True
            q.put((curX, curY))
        #move right
        curX = u[0] + 1
        curY = u[1]
        if (notOutOfBound(curX,curY, w, h) and
            graph[curY][curX] == '.' and not visited[curY][curX]):
            t += 1
            visited[curY][curX] = True
            q.put((curX, curY))
    return t

for i in range(1,t+1):
    w, h = map(int, input().split())
    visited = [[False for i in range(w)] for i in range(h)]
    graph = [['.' for i in range(w)] for i in range(h)]
    startX = 0
    startY = 0
    for j in range(h):
        line = list(input())
        for k in range(w):
            graph[j][k] = line[k]
            if (graph[j][k] == '@'):
                startX = k
                startY = j
                visited[j][k] = True
    
    print('Case ' + str(i) + ": " + str(BFS(startX, startY, graph, visited, w, h)))
