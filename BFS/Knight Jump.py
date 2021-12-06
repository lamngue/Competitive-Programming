import queue
n = int(input())
visited = [[False for i in range(n)] for i in range(n)]
graph = [['' for i in range(n)] for i in range(n)]
dist = [[0 for i in range(n)] for i in range(n)]

def notOutOfBound(x, y, w, h):
    return x >= 0 and y >= 0 and x < w and y < h

dx = [2, 2, -2, -2, 1, 1, -1, -1]
dy = [1, -1, 1, -1, 2, -2, 2, -2]

def BFS(x, y, graph, visited, w, h):
    q = queue.Queue()
    q.put((x, y))
    while not q.empty():
        ux, uy = q.get()
        if ux == 0 and uy == 0:
            return dist[uy][ux]
        for i in range(8):
            x = ux + dx[i]
            y = uy + dy[i]
            if notOutOfBound(x, y, n, n) and graph[y][x] == '.':
                if not visited[y][x]:
                    dist[y][x] = dist[uy][ux] + 1
                    visited[y][x] = True
                    q.put((x, y))
    return -1
    
startX = 0
startY = 0
for j in range(n):
    line = list(input())
    for k in range(n):
        graph[j][k] = line[k]
        if (graph[j][k] == 'K'):
            startX = k
            startY = j
            visited[j][k] = True
steps = BFS(startX, startY, graph, visited, n, n)
print(steps if steps != -1 else -1)
