import queue
class Node:
    def __init__(self, id, dist):
        self.dist = dist
        self.id = id
    def __lt__(self, other):
        return self.dist <= other.dist
INF = 1001
graph = [[] for i in range(INF)]
dist = [INF for i in range(INF)]
path = [-1 for i in range(INF)]
visited = [False for i in range(INF)]
def prims(src):
    pq = queue.PriorityQueue()
    pq.put(Node(src, 0))
    dist[src] = 0
    while pq.empty() == False:
        top = pq.get()
        u = top.id
        visited[u] = True
        for neighbor in graph[u]:
            v = neighbor.id
            w = neighbor.dist
            if visited[v] == False and w < dist[v]:
                dist[v] = w
                pq.put(Node(v, w))
                path[v] = u

def printMST(t):
    ans = 0
    for i in range(t):
        if path[i] == -1:
            continue
        ans += dist[i]
    return ans

t = int(input())
for i in range(t):
    input()
    dic = {}
    num = 0
    costs = []
    m = int(input())
    for j in range(m):
        l = input().split()
        city1 = l[0]
        city2 = l[1]
        c = int(l[2])
        if l[0] not in dic:
            dic[l[0]] = num
            num += 1
        if l[1] not in dic:
            dic[l[1]] = num
            num += 1
        graph[dic[l[0]]].append(Node(dic[l[1]], c))
        graph[dic[l[1]]].append(Node(dic[l[0]], c))
    prims(0)
    ans = printMST(len(dic))
    print(dist)
    for j in range(len(dic)):
        if dist[j] == INF:
            ans = "Impossible"
            break
    print("Case " + str(i+1) + ": " + str(ans))
    graph = [[] for i in range(INF)]
    dist = [INF for i in range(INF)]
    path = [-1 for i in range(INF)]
    visited = [False for i in range(INF)]   

