import queue
#use max heap
@total_ordering
class PQEntryMax:
    def __init__(self, char, value, firstPos):
        self.char = char
        self.value = value
        self.firstPos = firstPos
    def __lt__(self, other):
        return self.value > other.value or (self.value == other.value and self.firstPos < other.firstPos)
    
s = input()
dic = {}
a = []
for i in range(len(s)):
    if s[i] in dic:
        dic[s[i]] += 1
    else:
        dic[s[i]] = 1

h = queue.PriorityQueue()
for i in dic:
    h.put(PQEntryMax(i,dic[i], s.index(i)))
out = ""
for i in range(len(h.queue)):
    out += h.get().char
print(out)
