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

def findRoot(point): #[-1,0,1,4,1,1]
    b = []
    if path[point] == -1:
        return point
    while True:
        b.append(point)
        point = path[point]
        if point == -1:
            break
    return b[len(b)-1]

def findDistance(s, f):
    distance = 0
    b = []
    if path[f] == -1:
        return -1
    while True:
        distance += dist[f]
        b.append(f)
        f = path[f]
        print(f, s)
        if f == s:
            b.append(s)
            break
    return distance

case = 0
while True:
    case += 1
    c, s, q = map(int, input().split())
    if (c == 0 and s == 0 and q == 0):
        break
    for i in range(s):
        c1, c2, d = map(int, input().split())
        graph[c1-1].append(Node(c2-1, d))
        graph[c2-1].append(Node(c1-1, d))
        
    for i in range(c):
        if (visited[i] == False):
            prims(i)
    print("Case #" + str(case))
    print(dist[:c])
    for j in range(q):
        f, t = map(int, input().split())
        if (findRoot(f-1) != findRoot(t-1)):
            print("no path")
        else:
            ans = findDistance(f-1, t-1)
            print(ans)
    graph = [[] for i in range(INF)]
    dist = [INF for i in range(INF)]
    path = [-1 for i in range(INF)]
    visited = [False for i in range(INF)]
