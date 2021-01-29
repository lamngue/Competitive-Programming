import queue
while True:
    n = int(input())
    if (n == 0):
        break
    q = queue.Queue()
    for i in range(1, n+1):
        q.put(str(i))
    discard = []
    while q.qsize() >= 2:
        value = q.get()
        discard.append(value)
        q.put(q.get()) #get element from top and put to bottom
    if(len(discard)==0):
        print("Discarded cards:")
    else:
        print("Discarded cards: " + ", ".join(discard))
    print("Remaining card: " + q.queue[0])
