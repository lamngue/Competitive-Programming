import queue

n = int(input())
a = list(map(int,input().split()))
##first = -1
##second = -1
##third = -1
##for i in range(len(a)):
##    cur = a[i]
##    if (cur > first):
##        third = second
##        second = first
##        first = cur
##    elif (cur > second):
##        third = second
##        second = cur
##    elif (cur > third):
##        third = cur
##    if (i < 2):
##        print(-1)
##    else:
##        print(first * second * third)
pq = queue.PriorityQueue()
for x in a:
    pq.put(-x)
for i in range(n):
    if (i < 2):
        print(-1)
        continue
    first = pq.get()
    second = pq.get()
    third = pq.get()
    print(-1*first*second*third)
    pq.put(first)
    pq.put(second)
    pq.put(third)
