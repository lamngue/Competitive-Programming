import math
class City:
    def __init__(self, dis, pop):
        self.dis = dis
        self.pop = pop
    def __lt__(self, other):
        return self.dis < other.dis
    def __repr__(self):
         return "{dis: %s, pop: %s}" % (self.dis, self.pop)
    def __str__(self):
        return "{dis: %s, pop: %s}" % (self.dis, self.pop)

def getDistance(x, y):
    return math.sqrt(x**2 + y**2)
cities = []
n, s = map(int, input().split())
for i in range(n):
    x, y, k = map(int, input().split())
    distance = getDistance(x, y)
    cities.append(City(distance, k))
cities.sort()
meet = 1000000
ans = 0
flag = False
for city in cities:
    s += city.pop
    ans = city.dis
    if (s >= meet):
        flag = True
        break
if (flag):
    print(ans)
else:
    print(-1)
