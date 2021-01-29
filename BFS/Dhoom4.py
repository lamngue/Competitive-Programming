import queue
start, finish = map(int, input().split())
n = int(input())
a = list(map(int, input().split()))

MAX = 100000
visited = [-1 for i in range(MAX)]


q = queue.Queue()
q.put(start)
visited[start] = 0 #0 second

flag = False
    
while not q.empty():
    e = q.get()
    if (e == finish or flag == True):
        break
    for i in range(n):
        val = (e * a[i]) % 100000
        if visited[val] == -1:
            visited[val] = visited[e] + 1
            q.put(val)
            if val == finish:
                flag = True

print(visited[finish])
