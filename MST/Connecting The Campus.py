import queue
import math
class Node:
    def __init__(self, id, dist):
        self.dist = dist
        self.id = id
    def __lt__(self, other):
        return self.dist <= other.dist
    def __repr__(self):
        return "{dist: %s, id: %s}" % (self.dist, self.id)
    def __str__(self):
        return "{dist: %s, id: %s}" % (self.dist, self.id)

INF = 751
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
                
def getDistance(x1, y1, x2, y2):
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

def printMST(t):
    ans = 0
    for i in range(t):
        if path[i] == -1:
            continue
        ans += dist[i]
    return ans

def searchBuilding(f, t, graph):
    for building in graph[f]:
        if building.id == t:
            return building
        
while True:
    try:
        n = int(input()) #number of buildings
        coors = []
        for i in range(n):
            x, y = map(int, input().split())
            pair = (x, y)
            coors.append(pair)
        for i in range(n):
            for j in range(i+1, n):
                dis = getDistance(coors[i][0], coors[i][1], coors[j][0], coors[j][1])
                graph[i].append(Node(j, dis))
                graph[j].append(Node(i, dis))
        m = int(input())
        for i in range(m):
            f, t = map(int, input().split())
            node1 = searchBuilding(f-1, t-1, graph)
            node1.dist = 0
            node2 = searchBuilding(t-1, f-1, graph)
            node2.dist = 0
        prims(0)
        ans = printMST(n)
        print("%.2f" % ans)
        graph = [[] for i in range(INF)]
        dist = [INF for i in range(INF)]
        path = [-1 for i in range(INF)]
        visited = [False for i in range(INF)]
    except EOFError:
        break
        
            
