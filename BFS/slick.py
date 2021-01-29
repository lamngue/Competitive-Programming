import queue

def notOutOfBound(x, y, m, n):
    return x >= 0 and y >= 0 and x < m and y < n


def BFS(i, j):
    start = (j ,i)
    q = queue.Queue()
    slicks = 0
    size = 0
    if (graph[i][j] == 1):
        size = 1
    q.put(start)
    visited[i][j] = True
    while not q.empty():
        u = q.get()
        #moveUp
        curX = u[0]
        curY = u[1] + 1
        if (notOutOfBound(curX, curY, m, n) and
            graph[curY][curX] == 1 and not visited[curY][curX]):
            size += 1
            visited[curY][curX] = True
            q.put((curX, curY))
        #move down
        curY = u[1] - 1
        if (notOutOfBound(curX,curY, m, n) and
            graph[curY][curX] == 1 and not visited[curY][curX]):
            size += 1
            visited[curY][curX] = True
            q.put((curX, curY))
        #move left
        curX = u[0] - 1
        curY = u[1]
        if (notOutOfBound(curX,curY, m, n) and
            graph[curY][curX] == 1 and not visited[curY][curX]):
            size += 1
            visited[curY][curX] = True
            q.put((curX, curY))
        #move right
        curX = u[0] + 1
        curY = u[1]
        if (notOutOfBound(curX,curY, m, n) and
            graph[curY][curX] == 1 and not visited[curY][curX]):
            size += 1
            visited[curY][curX] = True
            q.put((curX, curY))
    return size

while True:
    n, m = map(int, input().split())
    if (n == 0 and m == 0):
        break
    graph = [[0 for i in range(m)] for i in range(n)]
    visited = [[False for i in range(m)] for i in range(n)]
    for i in range(n):
        line = list(input().split())
        for j in range(m):
            graph[i][j] = int(line[j])

    start = (0, 0)
    q = queue.Queue()
    size = 0
    l = []
    for i in range(n):
        for j in range(m):
            if (graph[i][j] == 1 and visited[i][j] == False):        
                size = BFS(i, j)
                l.append(size)
    l.sort()
    print(len(l))
    dic = {}
    for i in range(len(l)):
        if l[i] in dic:
            dic[l[i]] += 1
        else:
            dic[l[i]] = 1
    for i in dic:
        print(i, dic[i])
