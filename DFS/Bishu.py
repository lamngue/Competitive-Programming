n = int(input())

MAX = 10000
visited = [False for i in range(MAX)]
path = [-1 for i in range(MAX)]
graph = [[] for i in range(MAX)]

def DFSRecursion(s):
    visited[s] = True
    for v in graph[s]:
        if not visited[v]:
            path[v] = s
            DFSRecursion(v)

def findDistance(s, f):
    distance = 0
    b = []
    if path[f] == -1:
        return -1
    while True:
        distance += 1
        b.append(f)
        f = path[f]
        if f == s:
            b.append(s)
            break
    return distance

for i in range(n-1):
    u, v = map(int, input().split())
    graph[u-1].append(v-1)
    graph[v-1].append(u-1)

q = int(input())
gals = []
distance = [0 for i in range(n)]

s = 0
ans = MAX
DFSRecursion(s)
minDistance = MAX
for i in range(1,n):
    distance[i] = findDistance(s, i)
for i in range(q):
    g = int(input()) - 1
    if (distance[g] < minDistance or (distance[g] == minDistance and g < ans)):
        minDistance = distance[g]
        ans = g

print(ans + 1)

