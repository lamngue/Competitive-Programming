import queue

MAX = 301
INF = int(1e9)
graph = [[] for i in range(MAX)]
dist = [INF for i in range(MAX)]

class Node:
    def __init__(self, id, dist):
        self.dist = dist
        self.id = id
    def __lt__(self, other):
        return self.dist <= other.dist
    def __repr__(self):
         return "{id: %s, dist: %s}" % (self.id, self.dist)
    def __str__(self):
        return "{id: %s, dist: %s}" % (self.id, self.dist)


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

n = int(input())
dic = {}
cnt = 0
#convert name to node
for i in range(n):
    names = input().split()
    for i in range(3):
        if names[i] not in dic:
            dic[names[i]] = cnt
            cnt += 1
    
    graph[dic[names[0]]].append(Node(dic[names[1]], 1))
    graph[dic[names[1]]].append(Node(dic[names[0]], 1))
    graph[dic[names[1]]].append(Node(dic[names[2]], 1))
    graph[dic[names[2]]].append(Node(dic[names[1]], 1))
    graph[dic[names[0]]].append(Node(dic[names[2]], 1))
    graph[dic[names[2]]].append(Node(dic[names[0]], 1))
s = 0
sortednames=sorted(dic.keys(), key=lambda x:x.lower())
for x in dic:
    if x == "Isenbaev":
        s = dic[x]
        break
Dijkstra(s)
for x in sortednames:
    if (dist[dic[x]] == INF):
        dist[dic[x]] = "undefined"
    print(x, str(dist[dic[x]]))
    
    
        
