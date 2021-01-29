import queue

n, m = map(int, input().split())
cats = list(map(int, input().split()))



def BFS(s):
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

def countConsecutiveCats(s, f):
    b = []
    count = 0
    if path[f] == -1:
        return 0
    while True:
        b.append(f)
        f = path[f]
        if f == s:
            b.append(s)
            break
    #count consecutive cats
    maxCount = 0
    i = 0
    while i < len(b):
        if (cats[b[i]] == 1):
            count += 1
        elif (cats[b[i]] == 0):
            count = 0
        maxCount = max(count, maxCount)
        i += 1
    return maxCount

visited = [False for i in range(n)]
path = [-1 for i in range(n)]
graph = [[] for i in range(n)]

for i in range(n-1):
    u, v = map(int, input().split())
    graph[u-1].append(v-1)
    graph[v-1].append(u-1)
s = 0
BFS(s)
valid = 0
consecutiveCats = []
count = 0
final = 0
for i in range(len(graph)):
    if len(graph[i]) == 1 and i != 0:
        count = countConsecutiveCats(s, i)
        if (count <= m):
            final += 1
print(final)
