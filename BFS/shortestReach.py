import queue

MAX = 1000

def BFS(s, V, graph, visited, path):
    for i in range(V):
        visited[i] = False
        path[i] = -1
    q = queue.Queue()
    visited[s] = True
    q.put(s)
    while not q.empty():
        u = q.get()
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                q.put(v)
                path[v] = u
    
def findDistance(s, f):
    distance = 0
    b = []
    if path[f] == -1:
        return -1
    while True:
        distance += 6
        b.append(f)
        f = path[f]
        if f == s:
            b.append(s)
            break
    return distance

q = int(input())
for i in range(q):
    V, E = map(int, input().split())
    visited = [False for i in range(V)]
    path = [0 for i in range(MAX)]
    graph = [[] for i in range(MAX)]
    for j in range(E):
        u, v = map(int, input().split())
        graph[u-1].append(v-1)
        graph[v-1].append(u-1)
    s = int(input()) - 1
    BFS(s, V, graph, visited, path)
    nodeToVisit = queue.Queue()
    for k in range(V):
        if k != s:
            nodeToVisit.put(k)
    while nodeToVisit.qsize() > 0:
        f = nodeToVisit.get()
        print(findDistance(s,f), end=" ")
    print()
