import queue
import sys
MAX_INT = sys.maxsize
MAX = 101
INF = int(1e9)
graph = [[] for i in range(MAX)]
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
        for neighbor in graph[u]:
            if w + neighbor.dist < distR[neighbor.id]:
                distR[neighbor.id] = w + neighbor.dist
                pq.put(Node(neighbor.id, distR[neighbor.id]))

t = int(input())
for i in range(t):
    n = int(input())
    r = int(input())
    for j in range(r):
        a, b = map(int, input().split())
        graph[a].append(Node(b, 1))
        graph[b].append(Node(a, 1))
    s, d = map(int, input().split())
    Dijkstra(s)
    DijkstraR(d)
    ans = MAX_INT
    maxSum = -1
    for k in range(n):
        maxSum = max(maxSum, dist[k] + distR[k])
    print("Case " + str(i+1) +": " +str(maxSum))
    graph = [[] for i in range(MAX)]
    dist = [INF for i in range(MAX)]
    distR = [INF for i in range(MAX)]
