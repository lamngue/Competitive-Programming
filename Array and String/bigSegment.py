import sys
n = int(input())

segments = []
for i in range(n):
    segments.append(list(map(int,input().split())))

def big(segments):
    
    minA = sys.maxsize
    maxB = 0
    for i in range(len(segments)):
        minA = min(minA, segments[i][0])
        maxB = max(maxB, segments[i][1])
    for i in range(len(segments)):
        if (segments[i][0] == minA and segments[i][1] == maxB):
            return i+1
    return -1

print(big(segments))
