import queue
import sys
MAX_INT = sys.maxsize
MAX = 10000
INF = int(1e9)
graph = [[] for i in range(MAX)]
graphR = [[] for i in range(MAX)]
dist = [INF for i in range(MAX)]
distR = [INF for i in range(MAX)]
class Node:
    def __init__(self, id, dist):
        self.dist = dist
        self.id = id
    def __lt__(self, other):
        return self.dist <= other.dist

def Dijkstra(s):
    pq = queue.PriorityQueue()
    pq.put(Node(s, 0))
    dist[s] = 0
    while pq.empty() == False:
        top = pq.get()
        u = top.id
        w = top.dist
        for neighbor in graph[u]:
            if w + neighbor.dist < dist[neighbor.id]:
                dist[neighbor.id] = w + neighbor.dist
                pq.put(Node(neighbor.id, dist[neighbor.id]))

def DijkstraR(s):
    pq = queue.PriorityQueue()
    pq.put(Node(s, 0))
    distR[s] = 0
    while pq.empty() == False:
        top = pq.get()
        u = top.id
        w = top.dist
        for neighbor in graphR[u]:
            if w + neighbor.dist < distR[neighbor.id]:
                distR[neighbor.id] = w + neighbor.dist
                pq.put(Node(neighbor.id, distR[neighbor.id]))


test = int(input())
for i in range(test):
    n, m, k, s, t = map(int, input().split())
    for j in range(m):
        a, b, w = map(int, input().split())
        graph[a-1].append(Node(b-1, w))
        graphR[b-1].append(Node(a-1, w))
    ans = MAX_INT
    Dijkstra(s-1)
    DijkstraR(t-1)
    for i in range(k):
        a, b, w = map(int, input().split())
        dist1 = dist[a-1] + w + distR[b-1]
        dist2 = dist[b-1] + w + distR[a-1]
        ans = min(dist[t-1],min(ans, min(dist1,dist2)))
    if (ans >= INF):
        ans = -1
    print(ans)
    graph = [[] for i in range(MAX)]
    graphR = [[] for i in range(MAX)]
    dist = [INF for i in range(MAX)]
    distR = [INF for i in range(MAX)]
            
            
                  
